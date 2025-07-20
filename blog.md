---
layout: default
title: All Blog Posts
permalink: /blog/
---

# 📰 All Blog Posts by Category

{% assign grouped = site.posts | group_by_exp: "post", "post.categories[0]" %}
{% for group in grouped %}
  {% case group.name %}
    {% when "theory" %} <h2>📘 Theory</h2>
    {% when "demo" %} <h2>🧪 Demos</h2>
    {% when "development" %} <h2>💻 Development</h2>
    {% when "vision" %} <h2>🌟 Vision</h2>
    {% when "modeling" %} <h2>🧠 Modeling</h2>
    {% when "updates" %} <h2>📰 Updates</h2>
    {% else %} <h2>{{ group.name | capitalize }}</h2>
  {% endcase %}
  <ul>
    {% for post in group.items %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a> – 
        <small>{{ post.date | date: "%B %d, %Y" }}</small><br/>
        {{ post.excerpt }}
      </li>
    {% endfor %}
  </ul>
{% endfor %}
