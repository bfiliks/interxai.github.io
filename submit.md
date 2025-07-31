---
layout: default
title: Submit Case Study
permalink: /submit/
---

# 📤 Submit a Case Study

We welcome contributions of case studies that showcase human-centered Explainable AI and intertextual critique.

Please fill out the form below. Your submission will be reviewed and may be featured on the InterXAI platform.

<style>
  .collapsible-help summary {
    font-weight: bold;
    cursor: pointer;
    position: relative;
    list-style: none;
  }

  .collapsible-help summary::marker,
  .collapsible-help summary::-webkit-details-marker {
    display: none;
  }

  .collapsible-help summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 0.5em;
    transition: transform 0.2s ease-in-out;
  }

  .collapsible-help[open] summary::before {
    transform: rotate(90deg);
  }

  .collapsible-help div {
    padding: 0.5rem 0 1rem 1rem;
    animation: fadeIn 0.3s ease-in-out;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<details class="collapsible-help">
  <summary>❓ What is a Case Study? What Should I Submit?</summary>
  <div>
    <p>A <strong>case study</strong> is a real or hypothetical example that illustrates how human-centered explainability and intertextual critique can be applied in AI contexts.</p>

    <h4>✅ Why Submit?</h4>
    <ul>
      <li>Build a diverse gallery of applied examples</li>
      <li>Highlight community innovations</li>
      <li>Stimulate new research and applications</li>
    </ul>

    <h4>📝 What to Include</h4>
    <ul>
      <li><strong>Title</strong> of your case study</li>
      <li><strong>Summary:</strong> What is it about? What model or dataset did you use?</li>
      <li><strong>Tags:</strong> E.g., "GPT-4, ethics, metaphor, SHAP, literary analysis"</li>
      <li><strong>Link or Upload:</strong> Submit your work as a PDF or a link (Google Doc, blog, GitHub, etc.)</li>
    </ul>

    <h4>📌 Tips</h4>
    <ul>
      <li>Showcase how a model was explained, critiqued, or reinterpreted</li>
      <li>Include visuals or commentary if possible</li>
      <li>You don’t have to be an expert—student work, exploratory ideas, and reflections are welcome!</li>
    </ul>
  </div>
</details>

<br>

<form name="case-study-submission" method="POST" enctype="multipart/form-data" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you/">
  <input type="hidden" name="form-name" value="case-study-submission" />

  <p style="display:none">
    <label>Don’t fill this out if you’re human: <input name="bot-field" /></label>
  </p>

  <p><label>Your Name:<br><input type="text" name="name" required></label></p>

  <p><label>Email:<br><input type="email" name="email" required></label></p>

  <p><label>Title of Case Study:<br><input type="text" name="title" required></label></p>

  <p><label>Summary:<br><textarea name="summary" rows="5" required></textarea></label></p>

  <p><label>Relevant Tags (comma-separated):<br><input type="text" name="tags"></label></p>

  <p><label>PDF Upload (optional):<br><input type="file" name="attachment" accept=".pdf,.doc,.docx,.txt,.md"></label></p>

  <p><label>OR Provide a Link to Case Study:<br><input type="url" name="link"></label></p>

  <p><button type="submit">📤 Submit Case Study</button></p>
</form>
