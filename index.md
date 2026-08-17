---
layout: home
title: Ravensworth Research
---

# Equity research, argued in the open.

<p class="lede">Initiation reports built the way the sell side builds them — a stated
thesis, the sector map that makes the thesis possible, a company deep dive, an
explicit model and valuation, the risks that would kill it, and the catalysts
that resolve it. Every published rating opens a dated position in the
<a href="{{ '/portfolio/' | relative_url }}">model portfolio</a>, so the record is
falsifiable rather than asserted.</p>

## Coverage

{% assign reports = site.research | sort: "date" | reverse %}
{% if reports.size == 0 %}
<p class="empty-state">Initiating coverage shortly — first report in progress.</p>
{% else %}
<div class="table-wrap">
<table class="coverage">
  <thead>
    <tr><th>Ticker</th><th style="text-align:left">Report</th><th>Rating</th><th>Target</th><th>Published</th></tr>
  </thead>
  <tbody>
  {% for r in reports %}
    <tr>
      <td><a href="{{ r.url | relative_url }}">{{ r.ticker }}</a></td>
      <td style="text-align:left">{{ r.title }}</td>
      <td><span class="badge {{ r.rating | downcase }}">{{ r.rating }}</span></td>
      <td>{{ r.target }}</td>
      <td>{{ r.date | date: "%d %b %Y" }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>
{% endif %}

## How this works

Research is produced by an AI analyst working from primary sources — SEC filings
and XBRL financials, earnings transcripts, options and price data, macro series,
and 13F ownership — not from summarising other people's notes. The
[method]({{ '/method/' | relative_url }}) page states what the process is, what
data feeds it, and where it is weakest.
