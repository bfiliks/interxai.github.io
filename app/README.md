# 🧠 InterXAI App

This is the application layer of the InterXAI project, enabling interactive explanation comparison, annotation, and intertextual critique.

## 🚀 Overview

The InterXAI App provides:
- Integration of SHAP and LIME for model explanation
- Human annotation interface for tagging and critique
- Intertextual linking to external corpora
- A comparison orchestrator for side-by-side visualization of human + machine insight

## 📁 Directory Structure

```
/app
│
├── run_app.py                 # Entry point for running the InterXAI dashboard
├── requirements.txt           # Required Python packages
│
├── /xai_engine                # SHAP, LIME, etc.
│   ├── shap_explainer.py      # SHAP-based model explainer
│   └── lime_explainer.py      # LIME-based model explainer
│
├── /annotation_layer          # Human-centered annotation modules
│   ├── annotator_ui.py        # Streamlit UI components for annotation
│   └── tag_handler.py         # Handles metaphor/references tagging
│
├── /intertextual_linker       # Intertextual reference detection
│   ├── linker.py              # Core linking logic to corpora
│   └── corpora_utils.py       # Tools for corpus integration
│
└── /comparison_orchestrator   # Side-by-side critique + dashboard rendering
    ├── merger.py              # Merges human + machine explanation
    └── dashboard.py           # Generates visual comparative insights
```

## 🛠️ Getting Started

```bash
pip install -r requirements.txt
streamlit run run_app.py
```

## 📬 Contributions

We're open to collaboration! Submit PRs, issues, or case studies.  
Visit [interxai.netlify.app](https://interxai.netlify.app) to learn more.
