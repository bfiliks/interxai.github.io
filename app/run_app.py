
import streamlit as st

st.set_page_config(page_title="InterXAI App", layout="wide")

st.title("🤖 InterXAI – Human-Centered Explainability Platform")

st.markdown("""
Welcome to **InterXAI**!

This is a prototype dashboard demonstrating core features of the InterXAI platform, including:
- 🧠 Model Explanation via SHAP or LIME
- ✋ Human Annotation Interface
- 🔗 Intertextual Linker for context-aware comparison
- 🧲 Comparison View of machine vs human interpretations

> Note: This is a minimal placeholder. Full functionality to be integrated in modules.

Explore, annotate, critique – the XAI revolution begins with *you*!
""")

# Placeholder example
st.subheader("🚧 Modules Coming Soon:")
st.markdown("- Upload a text sample or prediction
- Visualize model explanation
- Annotate model outputs
- Link intertextual sources
- Export annotated results")
