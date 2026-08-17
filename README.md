# Claude Equity Researcher

AI-led equity research, published with a live model portfolio.
Site: https://ryanrodrigues25200525-svg.github.io/claude-equity-researcher/

## Adding a report

Create `_research/YYYY-MM-DD-ticker.md` with frontmatter:

```yaml
---
ticker: NVDA
company: NVIDIA Corporation
title: Short thesis-shaped headline
kind: Initiation of Coverage
sector: Semiconductors
rating: Buy          # Buy | Hold | Sell
price: $304.72
target: $420.00
upside: +38%
market_cap: $4.5tn
horizon: 12 months
date: 2026-08-17
data_as_of: 17 Aug 2026
summary: One-sentence thesis for the research index.
---
```

Then append the position to `data/positions.csv` and run the refresh.

## Portfolio

`data/positions.csv` is the source of truth — it opens in Excel or Numbers.
`scripts/update_portfolio.py` re-prices it against Yahoo's keyless quote endpoint
and rewrites the table between the `PORTFOLIO:START` / `PORTFOLIO:END` markers in
`portfolio.md`, appending the day's equity to `data/equity_curve.csv`.

```bash
python3 scripts/update_portfolio.py          # refresh marks
python3 scripts/update_portfolio.py --check  # self-check, writes nothing
```

Runs automatically on weekdays at 21:30 UTC via `.github/workflows/portfolio.yml`.

Closing a position: set `status` to `closed` and fill `close_date` and
`close_price`. Never delete a row — the record stays.

## Local preview

```bash
bundle install && bundle exec jekyll serve
```
