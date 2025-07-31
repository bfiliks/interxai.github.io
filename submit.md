---
layout: default
title: Submit Case Study
permalink: /submit/
---

# 📤 Submit a Case Study

We welcome contributions of case studies that showcase human-centered Explainable AI and intertextual critique.

Please fill out the form below. Your submission will be reviewed and may be featured on the InterXAI platform.

<details>
  <summary><strong>❓ What is a Case Study? What Should I Submit?</strong></summary>

  <div style="margin-top: 1rem;">

  A case study is a real or hypothetical example that illustrates how human-centered explainability and intertextual critique can be applied in AI contexts.

  ### ✅ Why Submit?
  Submitting helps InterXAI:
  - Build a diverse gallery of applied examples  
  - Highlight community innovations  
  - Stimulate new research and applications  

  ### 📝 What to Include
  - **Title** of your case study  
  - **Summary**: What is it about? What model or dataset did you use?  
  - **Tags**: E.g., "GPT-4, ethics, metaphor, SHAP, literary analysis"  
  - **Link or Upload**: Submit your work as a PDF or a link (Google Doc, blog, GitHub, etc.)

  ### 📌 Tips
  - Showcase how a model was explained, critiqued, or reinterpreted  
  - Include visuals or commentary if possible  
  - You don’t have to be an expert—experiences, student work, or exploratory ideas are welcome!

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
