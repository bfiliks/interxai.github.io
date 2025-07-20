---
layout: default
title: Home
---

<section style="padding: 2rem; background: #f8f9fa; border-radius: 10px;">
  <h1 style="font-size: 2.5rem;">Welcome to InterXAI</h1>
  <p style="font-size: 1.2rem;">A platform for human-centered AI critique and intertextual interpretation.</p>
  <a href="{{ site.baseurl }}/blog/" style="padding: 0.5rem 1rem; background: #007acc; color: white; border-radius: 5px; text-decoration: none;">📰 Read the Blog</a>
</section>

<section style="margin-top: 2rem;">
  <h2>🔍 What You Can Do with InterXAI</h2>
  <ul>
    <li>Compare <strong>machine-generated</strong> and <strong>human-critical</strong> explanations</li>
    <li>Explore intertextuality across model outputs and literary critique</li>
    <li>Annotate and visualize AI explanations</li>
    <li>Collaborate on building responsible AI tools</li>
  </ul>
</section>

<section style="margin-top: 2rem;">
  <h2>📝 Latest Blog Posts</h2>
  <ul>
    {% for post in site.posts limit:3 %}
      <li>
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> – 
        <small>{{ post.date | date: "%B %d, %Y" }}</small>
      </li>
    {% endfor %}
  </ul>
  <a href="{{ site.baseurl }}/blog/">See All Posts →</a>
</section>

<section style="margin-top: 2rem; padding: 1rem; border: 1px solid #ccc; border-radius: 10px;">
  <h2>🤝 Collaborate with Us</h2>
  <p>We welcome contributions from researchers, developers, educators, and humanities scholars interested in AI critique and explainability.</p>
  <a href="{{ site.baseurl }}/collaborate/">🔗 Learn More →</a>
</section>

<section style="margin-top: 3rem; border-top: 1px solid #ccc; padding-top: 2rem;">
  <h2>👤 Project Lead</h2>
  <div style="display: flex; align-items: center; gap: 1rem;">
    <img src="{{ site.baseurl }}/assets/img/felix-profile.jpg" alt="Felix B. Oke" style="width: 120px; height: 120px; border-radius: 50%; border: 2px solid #ccc;">
    <div>
      <p><strong>Felix B. Oke</strong> is the founder and project lead of InterXAI. With expertise in Digital Humanities, Natural Language Processing, and Explainable AI, Felix is dedicated to bridging critical human insight with algorithmic transparency. He leads the design and development of tools that foreground interpretability and accountability in machine learning systems.</p>
      <p>📧 <a href="mailto:bfiliks4xt@gmail.com">bfiliks4xt@gmail.com</a> |
         🔗 <a href="https://github.com/bfiliks" target="_blank">GitHub</a> |
         🌐 <a href="https://www.linkedin.com/in/felixoke/" target="_blank">LinkedIn</a></p>
    </div>
  </div>
</section>

<p style="text-align: right; font-size: 0.9rem;"><em>🌗 Try switching themes above.</em></p>
