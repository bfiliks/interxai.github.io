---
layout: default
title: All Blog Posts
permalink: /blog/
---

# 📰 All Blog Posts

Browse all blog updates from the InterXAI project:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> – 
      <small>{{ post.date | date: "%B %d, %Y" }}</small><br/>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
