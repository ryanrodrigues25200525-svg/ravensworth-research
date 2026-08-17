---
layout: home
title: Claude Equity Researcher
---

**AI-led equity research.** Initiation reports built the way the sell side builds
them — a stated thesis, the sector map that makes the thesis possible, a company
deep dive, an explicit model and valuation, the risks that would kill it, and the
catalysts that resolve it. Every published rating opens a dated position in the
[model portfolio]({{ '/portfolio/' | relative_url }}), so the track record is
falsifiable rather than asserted.

## Coverage

{% assign reports = site.research | sort: "date" | reverse %}
{% if reports.size == 0 %}
*Initiating coverage shortly. First report in progress.*
{% else %}
<table class="coverage">
  <thead>
    <tr><th>Ticker</th><th>Report</th><th>Rating</th><th>Target</th><th>Published</th></tr>
  </thead>
  <tbody>
  {% for r in reports %}
    <tr>
      <td><a href="{{ r.url | relative_url }}">{{ r.ticker }}</a></td>
      <td style="text-align:left">{{ r.title }}</td>
      <td class="rating {{ r.rating | downcase }}">{{ r.rating }}</td>
      <td>{{ r.target }}</td>
      <td>{{ r.date | date: "%d %b %Y" }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
{% endif %}

## How this works

Research is produced by an AI analyst working from primary sources — SEC filings
and XBRL financials, earnings transcripts, options and price data, macro series,
and 13F ownership — not from summarising other people's notes. The
[method]({{ '/method/' | relative_url }}) page states what the process is, what
data feeds it, and where it is weakest.
