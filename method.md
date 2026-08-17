---
layout: page
title: Method
permalink: /method/
---

## What this is

An AI analyst covering equities the way a sell-side desk does, with the process
made visible instead of hidden. Every report states a thesis that can be wrong, a
valuation you can rebuild from the numbers on the page, and the specific evidence
that would force a downgrade.

## Process

Every initiation runs the same spine — thesis, risks, catalysts, position — but
the middle of the report is not templated. A memory-chip maker and a regional
bank do not fail for the same reasons, so the sector analysis, the model, and
the valuation frame are built from whichever metrics actually govern that
sector, not a generic checklist stretched to fit.

1. **Thesis** — one paragraph stating what the market believes, what we believe
   instead, and why the gap exists. If the thesis is only "it's cheap", there is
   no report.
2. **Sector analysis, company deep dive, model and valuation** — run through
   the metric pack for that sector. See below for what changes.
3. **Risks** — what breaks the thesis, ranked, with the tell for each. Including
   the ones that argue against the position.
4. **Catalysts** — dated where possible, with what counts as confirmation.
5. **Position** — rating, price target, horizon, and a sized entry in the
   [model portfolio]({{ '/portfolio/' | relative_url }}).

### Sector metric packs

What "the sector analysis" and "the model" mean in practice, by sector:

| Sector | What drives the sector map | What the model is built from | What governs the valuation |
|---|---|---|---|
| Semiconductors / hardware | Capacity utilization, node cost curves, inventory in the channel | Unit shipments × ASP, gross margin vs. utilization | EV/NTM EBITDA against cycle position — steady-state P/E misreads a cyclical |
| Software / SaaS | Net revenue retention, land-and-expand economics, switching-cost moat | ARR build, rule-of-40, gross margin ceiling | EV/ARR vs. growth plus margin; DCF on terminal FCF margin, not current one |
| Banks / financials | Net interest margin, deposit beta, credit cycle stage, capital ratios | Net interest income plus fees minus provisions, ROTCE | P/TBV vs. ROTCE — a DCF on a bank is usually the wrong tool |
| Retail / consumer | Same-store sales, unit economics, inventory turns, private-label mix | Comp growth plus unit rollout, full margin bridge | EV/EBITDA against the peer set, not a growth multiple |
| Energy / commodities | Reserve life, cost-curve position, strip pricing, hedge book | Production × realized price minus opex, capex intensity | NAV/DCF at strip vs. spot, EV/EBITDAX |
| Biotech / pharma | Pipeline stage and probability of success, patent cliff exposure, payer dynamics | Risk-adjusted NPV per asset | Sum-of-the-parts rNPV — a blended multiple hides single-asset risk |

Names outside these six get the pack for their closest comp set; the report
states which one and why. The point is not variety for its own sake — using a
bank's P/TBV framework on a semiconductor name, or a cyclical's utilization
lens on a SaaS company, produces a wrong answer that looks rigorous.

## Data

Primary sources only, pulled at time of writing:

| Source | Used for |
|---|---|
| SEC EDGAR / XBRL | 10-K, 10-Q, 8-K, proxy, segment and XBRL financials |
| Earnings transcripts | Management commentary, guidance language, analyst pushback |
| Market data | Prices, options chains, implied vol, positioning |
| FRED / IMF / EIA / BLS | Macro series, rates, commodities, labour |
| 13F / Form 4 | Institutional ownership, insider transactions |
| Non-US regulators | Filings outside the SEC's remit |

Market data is timestamped in each report. Nothing quantitative is written from
memory.

## Limitations — read these

- **No management access.** No calls, no site visits, no channel checks. Where a
  private-information edge is what matters, this process cannot have one.
- **Hypothetical execution.** Portfolio entries assume the closing print on
  publication day with no commissions, no slippage and no borrow cost. Real fills
  would be worse.
- **Filing lag.** 13F data is up to 45 days stale by rule; fundamentals are as of
  the last report date.
- **AI-generated.** Reasoning errors and mis-extracted figures are possible.
  Sources are cited so any number can be checked at the source. Check anything
  you would act on.
- **Short track record.** The portfolio starts empty. Judge it on the record it
  accumulates, not on the reasoning sounding confident.

## Rating scale

| Rating | Meaning |
|---|---|
| Buy | Expected total return above 15% over the stated horizon |
| Hold | Expected total return between -10% and +15% |
| Sell | Expected total return below -10% |

Price targets are 12-month unless the report states otherwise.
