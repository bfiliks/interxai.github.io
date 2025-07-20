---
layout: default
title: All Blog Posts
permalink: /blog/
---

# 📰 All Blog Posts

{% assign grouped = site.posts | group_by_exp: "post", "post.categories[0]" %}
{% for group in grouped %}
  <h2>{{ group.name | capitalize }}</h2>
  <ul>
    {% for post in group.items %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a> – 
        <small>{{ post.date | date: "%B %d, %Y" }}</small>
        <br/>{{ post.excerpt }}
      </li>
    {% endfor %}
  </ul>
{% endfor %}
