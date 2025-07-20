---
layout: default
title: Home
---

# Welcome to InterXAI

A platform for human-centered AI critique and intertextual interpretation.

---

## 📝 Latest Blog Posts

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> – 
      <small>{{ post.date | date: "%B %d, %Y" }}</small><br/>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
