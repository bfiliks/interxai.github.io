# run_app.py

import streamlit as st
import pandas as pd
import altair as alt
import base64

# Import SHAP and LIME explainer modules
from xai_engine.shap_explainer import SHAPExplainer
from xai_engine.lime_explainer import LIMEExplainer

# Page configuration
st.set_page_config(page_title="InterXAI App", layout="wide")
st.title("🤖 InterXAI – Human-Centered Explainability Platform")

st.markdown("""
Welcome to **InterXAI**!

This prototype dashboard demonstrates core features of the InterXAI platform:
- 🧠 Model Explanation via SHAP or LIME
- ✋ Human Annotation Interface
- 🔗 Intertextual Linker
- 🧲 Comparison View of machine vs. human interpretations

> Explore, annotate, critique – the XAI revolution begins with *you*!
""")

# --- Tabs for Navigation ---
tab1, tab2, tab3 = st.tabs(["📥 Upload Text", "🔍 Compare SHAP & LIME", "⚙️ Settings"])

# --- Tab 1: Upload or Paste Text ---
with tab1:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    input_text = st.text_area("Or paste your text here:", height=150)

    if uploaded_file is not None:
        input_text = uploaded_file.read().decode("utf-8")
        st.success("File uploaded and loaded into the text area.")

# --- Tab 2: SHAP vs. LIME Live Comparison ---
with tab2:
    st.subheader("SHAP vs. LIME Comparison View")

    if not input_text:
        st.info("Upload or enter text in Tab 1 to see explanations.")
    else:
        shap_exp = SHAPExplainer().explain(input_text)
        lime_exp = LIMEExplainer().explain(input_text)

        if "error" in shap_exp or "error" in lime_exp:
            st.error(f"Explanation failed.\n\nSHAP Error: {shap_exp.get('error')}\nLIME Error: {lime_exp.get('error')}")
        else:
            tokens = list(set(shap_exp["tokens"]).intersection(set(lime_exp["tokens"])))
            data = {
                "tokens": tokens,
                "shap_importance": [shap_exp["importance"][shap_exp["tokens"].index(tok)] for tok in tokens],
                "lime_weights": [lime_exp["weights"][lime_exp["tokens"].index(tok)] for tok in tokens]
            }

            df = pd.DataFrame(data)

            chart = alt.Chart(df).transform_fold(
                ["shap_importance", "lime_weights"],
                as_=["method", "importance"]
            ).mark_bar().encode(
                x=alt.X("tokens:N", title="Token"),
                y=alt.Y("importance:Q", title="Importance"),
                color=alt.Color("method:N", title="Explanation Method"),
                tooltip=["tokens:N", "method:N", "importance:Q"]
            ).properties(
                width=700,
                height=400,
                title="SHAP vs. LIME Token-Level Explanation"
            )

            st.altair_chart(chart, use_container_width=True)

# --- Tab 3: Settings ---
with tab3:
    st.subheader("Settings")
    st.info("Settings and advanced configuration options will appear here.")

# --- Download Input Text ---
if input_text:
    st.markdown("### 📄 Download Your Input")
    b64 = base64.b64encode(input_text.encode()).decode()
    st.markdown(
        f'<a href="data:file/txt;base64,{b64}" download="input_text.txt">📥 Download Input Text</a>',
        unsafe_allow_html=True
    )
