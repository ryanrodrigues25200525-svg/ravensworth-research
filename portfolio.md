---
layout: page
title: Model Portfolio
permalink: /portfolio/
---

Every published rating opens a position here at the closing price on the day the
report goes out. Nothing is added retroactively and nothing is quietly dropped —
closed positions stay on the page with their realised result. Starting capital is
$1,000,000. Positions are sized by conviction, not equally.

Marks are refreshed automatically on trading days after the US close. The source
of truth is [`data/positions.csv`](https://github.com/ryanrodrigues25200525-svg/ravensworth-research/blob/main/data/positions.csv),
which opens directly in Excel or Numbers.

<!-- PORTFOLIO:START -->
<div class="stat-strip">
<div class="stat-tile"><span class="stat-label">Equity</span><span class="stat-value">$1,000,000</span></div>
<div class="stat-tile"><span class="stat-label">Total return</span><span class="stat-value"><span class="pos">+0.0%</span></span></div>
<div class="stat-tile"><span class="stat-label">Unrealised P&amp;L</span><span class="stat-value">$0</span></div>
<div class="stat-tile"><span class="stat-label">Realised P&amp;L</span><span class="stat-value">$0</span></div>
<div class="stat-tile"><span class="stat-label">Open positions</span><span class="stat-value">1</span></div>
<div class="stat-tile"><span class="stat-label">Gross exposure</span><span class="stat-value">3%</span></div>
<div class="stat-tile"><span class="stat-label">Net exposure</span><span class="stat-value">3%</span></div>
</div>
<h3>Open positions</h3>
<div class="table-wrap"><table class="ledger"><thead><tr><th>Ticker</th><th>L/S</th><th>Rating</th><th>Opened</th><th>Entry</th><th>Mark</th><th>Target</th><th>Weight</th><th>Return</th><th>P&amp;L</th></tr></thead><tbody>
<tr><td><a href="{{ '/research/2026-08-18-mu/' | relative_url }}">MU</a></td><td><span class="direction long">L</span></td><td><span class="badge hold">Hold</span></td><td>2026-08-18</td><td>$1,011.75</td><td>$1,011.75</td><td>$940.00</td><td>2.5%</td><td><span class="pos">+0.0%</span></td><td>$0</td></tr>
</tbody></table></div>
<p class="stamp">Marks refreshed 17 Aug 2026 21:48 UTC.</p>
<!-- PORTFOLIO:END -->

<div class="disclaimer">
<strong>Hypothetical performance.</strong> This is a paper portfolio. No capital is
at risk and no orders are routed to any venue. Marks are last trade or previous
close from public sources, not executable prices. Results assume the stated entry
price with no commissions, no slippage, no borrow cost on shorts, no dividends and
no taxes — real-world execution would differ, generally for the worse. Hypothetical
results are not indicative of future returns. See <a href="{{ '/disclosures/' | relative_url }}">full disclosures</a>.
</div>
