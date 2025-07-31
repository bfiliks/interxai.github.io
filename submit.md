---
layout: default
title: Submit Case Study
permalink: /submit/
---

# 📤 Submit a Case Study

We welcome contributions of case studies that showcase human-centered Explainable AI and intertextual critique.  
Please fill out the form below. Your submission will be reviewed and may be featured on the InterXAI platform.

<style>
  .submit-container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    margin-top: 2rem;
  }

  .form-column {
    flex: 1 1 500px;
    min-width: 300px;
  }

  .faq-column {
    flex: 1 1 300px;
    min-width: 280px;
    background: var(--card);
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.05);
  }

  .faq-column h3 {
    margin-top: 0;
  }

  .faq-column details {
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    background: white;
  }

  [data-theme="dark"] .faq-column details {
    background: var(--bg);
    border-color: #444;
  }

  .faq-column summary {
    font-weight: bold;
    cursor: pointer;
    list-style: none;
  }

  .faq-column summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 0.5em;
    transition: transform 0.2s ease-in-out;
  }

  .faq-column details[open] summary::before {
    transform: rotate(90deg);
  }

  .faq-column details div {
    padding: 0.5rem 0 0.5rem 1rem;
  }
</style>

<div class="submit-container">
  <div class="form-column">

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

  </div>

  <div class="faq-column">
    <h3>❓ Frequently Asked Questions</h3>

    <details>
      <summary>What is a case study?</summary>
      <div>
        A <strong>case study</strong> is a real or hypothetical example that demonstrates how human-centered explainability and intertextual critique can be applied in AI contexts.
      </div>
    </details>

    <details>
      <summary>Why should I submit one?</summary>
      <div>
        <ul>
          <li>Contribute to a growing gallery of practical examples</li>
          <li>Inspire others in the community</li>
          <li>Promote interdisciplinary research and creativity</li>
        </ul>
      </div>
    </details>

    <details>
      <summary>What should I include?</summary>
      <div>
        <ul>
          <li><strong>Title</strong> of your case study</li>
          <li><strong>Summary</strong>: What is it about? What model or dataset did you use?</li>
          <li><strong>Tags</strong>: E.g., “GPT-4, ethics, metaphor, SHAP”</li>
          <li><strong>Link or Upload</strong>: PDF or link (Google Doc, GitHub, blog, etc.)</li>
        </ul>
      </div>
    </details>

    <details>
      <summary>Who can submit?</summary>
      <div>
        Anyone! Submissions are welcome from students, educators, researchers, artists, and practitioners.
      </div>
    </details>

    <details>
      <summary>What happens after submission?</summary>
      <div>
        Your submission will be reviewed by the InterXAI team. If accepted, it may appear on our <a href="/case-studies/">Case Studies</a> page.
      </div>
    </details>
  </div>
</div>
