---
layout: default
title: Submit Case Study
permalink: /submit/
---

# 📤 Submit a Case Study

We welcome contributions of case studies that showcase human-centered Explainable AI and intertextual critique.

Please fill out the form below. Your submission will be reviewed and may be featured on the InterXAI platform.

<form name="case-study-submission" method="POST" enctype="multipart/form-data" data-netlify="true" netlify-honeypot="bot-field" action="/interxai.github.io/thank-you/">
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
