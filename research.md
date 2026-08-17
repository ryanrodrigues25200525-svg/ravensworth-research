---
layout: page
title: Research
permalink: /research/
---

{% assign reports = site.research | sort: "date" | reverse %}
{% if reports.size == 0 %}
*Initiating coverage shortly.*
{% else %}
{% for r in reports %}
### [{{ r.ticker }} — {{ r.title }}]({{ r.url | relative_url }})

<span class="stamp">{{ r.kind | default: "Initiation" }} &middot; {{ r.date | date: "%d %b %Y" }}
&middot; <span class="rating {{ r.rating | downcase }}">{{ r.rating }}</span>
&middot; target {{ r.target }} ({{ r.upside }})</span>

{{ r.summary }}

{% endfor %}
{% endif %}
