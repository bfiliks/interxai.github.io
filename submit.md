---
layout: default
title: Submit Case Study
permalink: /submit/
---

# 📤 Submit a Case Study

We welcome contributions of case studies that showcase human-centered Explainable AI and intertextual critique.

Please fill out the form below. Your submission will be reviewed and may be featured on the InterXAI platform.

<style>
  .faq-section {
    margin-bottom: 2rem;
    padding: 1rem;
    background: var(--card);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.04);
  }

  .faq-section details {
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    background: white;
    transition: background 0.3s;
  }

  [data-theme="dark"] .faq-section details {
    background: var(--bg);
    border-color: #444;
  }

  .faq-section summary {
    font-weight: bold;
    cursor: pointer;
    list-style: none;
    position: relative;
  }

  .faq-section summary::marker,
  .faq-section summary::-webkit-details-marker {
    display: none;
  }

  .faq-section summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 0.5em;
    transition: transform 0.2s ease-in-out;
  }

  .faq-section details[open] summary::before {
    transform: rotate(90deg);
  }

  .faq-section details div {
    padding: 0.5rem 0 0.5rem 1rem;
    animation: fadeIn 0.3s ease-in-out;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<div class="faq-section">
  <h3>❓ Frequently Asked Questions about Case Study Submissions</h3>

  <details>
    <summary>What is a case study?</summary>
    <div>
      A <strong>case study</strong> is a real or hypothetical example that demonstrates how human-centered explainability and intertextual critique can be applied in AI contexts. It could involve a project, analysis, or even a classroom experiment.
    </div>
  </details>

  <details>
    <summary>Why should I submit a case study?</summary>
    <div>
      Submitting helps InterXAI:
      <ul>
        <li>Build a diverse gallery of applied examples</li>
        <li>Highlight community innovations</li>
        <li>Stimulate new research and applications</li>
      </ul>
    </div>
  </details>

  <details>
    <summary>What should I include in my submission?</summary>
    <div>
      <ul>
        <li><strong>Title</strong> of your case study</li>
        <li><strong>Summary:</strong> What is it about? What model or dataset did you use?</li>
        <li><strong>Tags:</strong> E.g., "GPT-4, ethics, metaphor, SHAP, literary analysis"</li>
        <li><strong>Link or Upload:</strong> Submit your work as a PDF or a link (Google Doc, blog, GitHub, etc.)</li>
      </ul>
    </div>
  </details>

  <details>
    <summary>Who can submit?</summary>
    <div>
      Anyone! We welcome students, researchers, practitioners, and creative thinkers. You don’t need to be an expert—exploratory projects and reflections are encouraged.
    </div>
  </details>

  <details>
    <summary>What happens after submission?</summary>
    <div>
      Your submission will be reviewed by our team. If selected, it will appear on our <a href="/case-studies/">Case Studies</a> page. We may follow up with you if more details are needed.
    </div>
  </details>
</div>

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
