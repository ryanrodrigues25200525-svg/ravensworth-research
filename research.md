---
layout: page
title: Research
permalink: /research/
---

{% assign reports = site.research | sort: "date" | reverse %}
{% if reports.size == 0 %}
<p class="empty-state">Initiating coverage shortly.</p>
{% else %}
{% for r in reports %}
<div class="research-entry">
  <h3><a href="{{ r.url | relative_url }}">{{ r.ticker }} — {{ r.title }}</a></h3>
  <p class="stamp">{{ r.kind | default: "Initiation" }} &middot; {{ r.date | date: "%d %b %Y" }}
    &middot; <span class="badge {{ r.rating | downcase }}">{{ r.rating }}</span>
    &middot; target {{ r.target }} ({{ r.upside }})</p>
  <p>{{ r.summary }}</p>
</div>
{% endfor %}
{% endif %}
