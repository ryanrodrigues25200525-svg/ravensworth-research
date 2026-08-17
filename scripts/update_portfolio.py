#!/usr/bin/env python3
"""Re-price data/positions.csv and rewrite the table inside portfolio.md.

Quotes come from Yahoo's keyless chart endpoint, so this runs in a bare GitHub
Action with no secrets.

    python3 scripts/update_portfolio.py          # refresh marks
    python3 scripts/update_portfolio.py --check  # run self-check, touch nothing
"""

import csv
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

ROOT = Path(__file__).resolve().parent.parent
POSITIONS = ROOT / "data" / "positions.csv"
CURVE = ROOT / "data" / "equity_curve.csv"
PAGE = ROOT / "portfolio.md"
START_CAPITAL = 1_000_000.0
START, END = "<!-- PORTFOLIO:START -->", "<!-- PORTFOLIO:END -->"


def quote(ticker):
    """Last price from Yahoo's keyless chart endpoint, or None if unknown."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=1d&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            meta = json.load(r)["chart"]["result"][0]["meta"]
    except (urllib.error.HTTPError, urllib.error.URLError, KeyError, TypeError):
        return None  # unknown symbol, or Yahoo having a moment
    px = meta.get("regularMarketPrice") or meta.get("previousClose")
    return float(px) if px else None


def pnl(entry, mark, shares, direction):
    """Signed P&L in dollars. Short is the mirror of long."""
    sign = -1.0 if direction.strip().lower() == "short" else 1.0
    return (mark - entry) * shares * sign


def money(x):
    return f"{'-' if x < 0 else ''}${abs(x):,.0f}"


def pct_span(x):
    return f'<span class="{"pos" if x >= 0 else "neg"}">{x:+.1f}%</span>'


def sparkline(points, w=640, h=120):
    """Inline SVG equity curve. points = [(date, equity), ...]"""
    if len(points) < 2:
        return ""
    vals = [v for _, v in points]
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    pad = 8
    step = (w - 2 * pad) / (len(vals) - 1)
    xy = [
        (pad + i * step, h - pad - (v - lo) / span * (h - 2 * pad))
        for i, v in enumerate(vals)
    ]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in xy)
    area = f"{pad},{h - pad} {line} {w - pad},{h - pad}"
    colour = "#0f6b47" if vals[-1] >= vals[0] else "#9a2b25"
    base = h - pad - (START_CAPITAL - lo) / span * (h - 2 * pad)
    baseline = (
        f'<line x1="{pad}" y1="{base:.1f}" x2="{w - pad}" y2="{base:.1f}" '
        f'stroke="#98a2b0" stroke-width="1" stroke-dasharray="3 3"/>'
        if lo <= START_CAPITAL <= hi
        else ""
    )
    return (
        f'<svg class="equity-curve" viewBox="0 0 {w} {h}" role="img" '
        f'aria-label="Model portfolio equity curve">'
        f'<polygon points="{area}" fill="{colour}" opacity="0.10"/>{baseline}'
        f'<polyline points="{line}" fill="none" stroke="{colour}" stroke-width="2"/>'
        f"</svg>"
    )


def render(rows, stamp):
    open_rows = [r for r in rows if r["status"].strip().lower() != "closed"]
    closed = [r for r in rows if r["status"].strip().lower() == "closed"]

    realised = sum(
        pnl(float(r["entry_price"]), float(r["close_price"]), float(r["shares"]), r["direction"])
        for r in closed
    )
    unrealised = sum(r["_pnl"] for r in open_rows)
    equity = START_CAPITAL + realised + unrealised
    gross = sum(abs(r["_mark"] * float(r["shares"])) for r in open_rows)
    net = sum(
        r["_mark"] * float(r["shares"]) * (-1 if r["direction"].strip().lower() == "short" else 1)
        for r in open_rows
    )

    out = [sparkline(read_curve())]
    out.append("| Metric | Value |\n|---|---|")
    out.append(f"| Equity | {money(equity)} |")
    out.append(f"| Total return | {pct_span((equity / START_CAPITAL - 1) * 100)} |")
    out.append(f"| Unrealised P&L | {money(unrealised)} |")
    out.append(f"| Realised P&L | {money(realised)} |")
    out.append(f"| Open positions | {len(open_rows)} |")
    out.append(f"| Gross exposure | {gross / equity * 100:.0f}% |" if equity else "")
    out.append(f"| Net exposure | {net / equity * 100:.0f}% |" if equity else "")

    if open_rows:
        out.append("\n### Open positions\n")
        out.append(
            "| Ticker | L/S | Rating | Opened | Entry | Mark | Target | Weight | Return | P&L |\n"
            "|---|---|---|---|---|---|---|---|---|---|"
        )
        for r in sorted(open_rows, key=lambda r: -abs(r["_pnl"])):
            entry, sh = float(r["entry_price"]), float(r["shares"])
            ret = r["_pnl"] / (entry * sh) * 100 if entry and sh else 0.0
            link = f"[{r['ticker']}]({{{{ '{r['report']}' | relative_url }}}})" if r["report"] else r["ticker"]
            out.append(
                f"| {link} | {r['direction'][:1].upper()} | {r['rating']} "
                f"| {r['open_date']} | ${entry:,.2f} | ${r['_mark']:,.2f} "
                f"| ${float(r['target_price']):,.2f} | {abs(r['_mark'] * sh) / equity * 100:.1f}% "
                f"| {pct_span(ret)} | {money(r['_pnl'])} |"
            )

    if closed:
        out.append("\n### Closed positions\n")
        out.append("| Ticker | L/S | Opened | Closed | Entry | Exit | Return | P&L |\n|---|---|---|---|---|---|---|---|")
        for r in closed:
            entry, ex, sh = float(r["entry_price"]), float(r["close_price"]), float(r["shares"])
            p = pnl(entry, ex, sh, r["direction"])
            out.append(
                f"| {r['ticker']} | {r['direction'][:1].upper()} | {r['open_date']} "
                f"| {r['close_date']} | ${entry:,.2f} | ${ex:,.2f} "
                f"| {pct_span(p / (entry * sh) * 100)} | {money(p)} |"
            )

    out.append(f'\n<p class="stamp">Marks refreshed {stamp}.</p>')
    return equity, "\n".join(x for x in out if x)


def read_curve():
    if not CURVE.exists():
        return []
    with CURVE.open() as f:
        return [(r["date"], float(r["equity"])) for r in csv.DictReader(f)]


def write_curve(equity, day):
    points = [p for p in read_curve() if p[0] != day] + [(day, equity)]
    with CURVE.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "equity"])
        w.writerows(sorted(points))


def main():
    with POSITIONS.open() as f:
        rows = [r for r in csv.DictReader(f) if r.get("ticker")]

    if not rows:
        print("no positions yet — nothing to do")
        return 0

    for r in rows:
        if r["status"].strip().lower() == "closed":
            continue
        mark = quote(r["ticker"])
        if mark is None:
            print(f"warning: no quote for {r['ticker']}, holding entry price as mark")
            mark = float(r["entry_price"])
        r["_mark"] = mark
        r["_pnl"] = pnl(float(r["entry_price"]), mark, float(r["shares"]), r["direction"])

    now = datetime.now(timezone.utc)
    equity, table = render(rows, now.strftime("%d %b %Y %H:%M UTC"))
    write_curve(equity, now.strftime("%Y-%m-%d"))

    page = PAGE.read_text()
    head, _, rest = page.partition(START)
    _, _, tail = rest.partition(END)
    PAGE.write_text(f"{head}{START}\n{table}\n{END}{tail}")
    print(f"equity {money(equity)} ({(equity / START_CAPITAL - 1) * 100:+.2f}%)")
    return 0


def check():
    assert pnl(100, 110, 10, "long") == 100, "long gain"
    assert pnl(100, 90, 10, "long") == -100, "long loss"
    assert pnl(100, 90, 10, "short") == 100, "short gain"
    assert pnl(100, 110, 10, "short") == -100, "short loss"
    assert money(-1234.6) == "-$1,235"
    assert sparkline([("d", 1.0)]) == "", "single point draws nothing"
    assert '<polyline' in sparkline([("a", 1.0), ("b", 2.0)])
    px = quote("AAPL")
    assert px and px > 0, "yahoo quote failed"
    assert quote("ZZZZNOTAREALTICKER") is None, "bad ticker should be None"
    print("self-check ok — AAPL last", px)


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else main())
