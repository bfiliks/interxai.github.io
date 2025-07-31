# run_app.py

import streamlit as st
from xai_engine.shap_explainer import SHAPExplainer
from xai_engine.lime_explainer import LIMEExplainer

st.set_page_config(page_title="InterXAI App", layout="wide")

st.title("🤖 InterXAI – Human-Centered Explainability Platform")

st.markdown("""
Welcome to **InterXAI** – a platform combining Explainable AI with intertextual critique.

This prototype demonstrates:
- 🧠 SHAP & LIME Model Explanations
- ✋ Human Annotation (coming soon)
- 🔗 Intertextual Linking (coming soon)
- 🧲 Comparison Dashboard (coming soon)

Explore, annotate, critique – the XAI revolution begins with *you*!
""")

# --- Text Input ---
st.subheader("📥 Enter Text for Explanation")
user_input = st.text_area("Paste your model-generated or user input text below:", height=150)

# --- Explanation Method Selection ---
method = st.selectbox("Choose Explanation Method:", ["Select...", "SHAP", "LIME"])

if user_input and method != "Select...":
    st.subheader(f"🔍 {method} Explanation")
    
    if method == "SHAP":
        explainer = SHAPExplainer()
        output = explainer.explain(user_input)
        if "error" in output:
            st.error(f"SHAP Error: {output['error']}")
        else:
            st.write("**Tokens:**", output["tokens"])
            st.write("**Importance:**", output["importance"])
            st.bar_chart(output["importance"])

    elif method == "LIME":
        explainer = LIMEExplainer()
        output = explainer.explain(user_input)
        if "error" in output:
            st.error(f"LIME Error: {output['error']}")
        else:
            st.write("**Tokens:**", output["tokens"])
            st.write("**Weights:**", output["weights"])
            st.bar_chart(output["weights"])

# --- Placeholder Modules ---
st.divider()
st.subheader("🚧 Modules Coming Soon:")
st.markdown("""
- 📝 Annotate model outputs with critique and reframing  
- 🔗 Link outputs to intertextual references  
- 📊 Visualize human vs machine understanding side-by-side  
- 🧾 Export to JSON/PDF for further use
""")
