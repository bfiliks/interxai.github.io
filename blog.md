---
layout: default
title: All Blog Posts
permalink: /blog/
---

# 📰 All Blog Posts by Category

<style>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}
.blog-card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 10px;
  background: #fff;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
}
.blog-card h3 {
  margin-top: 0;
}
.blog-card a {
  text-decoration: none;
  color: #007acc;
}
</style>

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

  <div class="blog-grid">
    {% for post in group.items %}
      <div class="blog-card">
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        <small>{{ post.date | date: "%B %d, %Y" }}</small>
        <p>{{ post.excerpt }}</p>
      </div>
    {% endfor %}
  </div>
{% endfor %}
