import streamlit as st
import pandas as pd
import altair as alt
import base64

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

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["📥 Upload Text", "🔍 Compare SHAP & LIME", "⚙️ Settings"])

# --- Upload or Paste Text ---
with tab1:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    input_text = st.text_area("Or paste your text here:", height=150)

    if uploaded_file is not None:
        input_text = uploaded_file.read().decode("utf-8")
        st.success("File uploaded and loaded into the text area.")

# --- SHAP vs LIME Comparison ---
with tab2:
    st.subheader("SHAP vs. LIME Comparison View")

    # Dummy explanation data
    sample_data = {
        "tokens": ["good", "AI", "model", "output", "unclear"],
        "shap_importance": [0.1, 0.4, 0.3, 0.1, 0.1],
        "lime_weights": [0.2, 0.3, 0.2, 0.1, 0.2]
    }

    # Ensure it's a native pandas DataFrame
    df = pd.DataFrame(sample_data)

    # Build Altair chart
    chart = alt.Chart(df).transform_fold(
        ["shap_importance", "lime_weights"],
        as_=["method", "importance"]
    ).mark_bar().encode(
        x=alt.X("tokens:N", title="Token"),
        y=alt.Y("importance:Q", title="Importance"),
        color=alt.Color("method:N", title="Explanation Method"),
        tooltip=["tokens:N", "method:N", "importance:Q"]
    ).properties(
        width=600,
        height=400,
        title="Explanation Comparison (SHAP vs LIME)"
    )

    st.altair_chart(chart, use_container_width=True)

# --- Settings Tab ---
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
