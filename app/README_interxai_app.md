
# 🧠 InterXAI App: Human-Centered Explainable AI Platform

Welcome to the `interxai.github.io/app` directory — the backend engine powering **InterXAI**’s core features for model interpretability and intertextual critique.

This app provides a modular, Streamlit-based interface to explore, annotate, and compare model explanations with human perspectives.

---

## 🚀 Features

### 🧠 XAI Engine
- Supports SHAP, LIME, and other popular model explanation tools
- Compatible with classification, regression, and generative models
- Built with extensibility for vision/multi-modal models via API integration

### ✋ Human Annotation Engine
- Allows users to annotate or critique AI outputs
- Tags metaphors, omissions, intertextual references, or biases
- Tracks agreement and divergence among annotators

### 🔗 Intertextual Linker
- Compares AI output with external texts (Wikipedia, books, archives)
- Detects reused phrasing, conceptual drift, and textual resonance

### 🧲 Comparison Orchestrator
- Merges model explanations and human annotations
- Visualizes insights using dashboards
- Enables export to PDF, JSON, or CSV for reports

---

## 📁 Directory Structure

```
app/
├── run_app.py               # Main Streamlit entry point
├── xai_engine/              # SHAP/LIME explanation logic
│   └── shap_explainer.py
├── annotation/              # Annotation and user interface logic
│   └── annotator_interface.py
├── intertextual/            # Text similarity & linking logic
│   └── similarity_engine.py
├── comparison/              # Reconciliation of machine vs human insights
│   └── comparator.py
└── assets/                  # Logos, sample data, visual icons
```

---

## ⚙️ Requirements

Make sure the following are installed (see `requirements.txt` for full list):

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

To launch the InterXAI Streamlit interface locally:

```bash
streamlit run run_app.py
```

---

## 🧪 Sample Use Case

1. Load a trained model and sample input (text or tabular)
2. Generate SHAP/LIME explanation
3. View model output and human critique side-by-side
4. Add or view intertextual links
5. Export insights for review or publication

---

## 🤝 Contributing

We welcome contributions! You can:
- Add new annotation types or explanation methods
- Improve UI components or visualizations
- Submit case studies via the [Submit Page](https://interxai.netlify.app/submit)

---

## 📄 License

This app is released under the **MIT License**.  
All research outputs are shared under **Creative Commons CC-BY-SA**.

---

## 📬 Contact

Felix B. Oke – [GitHub](https://github.com/bfiliks) | [Email](mailto:bfiliks4xt@gmail.com)  
Project Website: [https://interxai.netlify.app](https://interxai.netlify.app)
