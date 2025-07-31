
"""
dashboard.py
Generates Streamlit dashboard to visualize human + model explanations side-by-side.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

def display_dashboard(data):
    st.title("InterXAI Comparison Dashboard")

    if data is None or data.empty:
        st.warning("No data available to display.")
        return

    st.subheader("Token Importance / Annotation Comparison")
    for i, row in data.iterrows():
        st.write(f"**Text**: {row.get('text', '')}")
        fig = px.bar(
            x=row.get('tokens', []),
            y=row.get('importance', []),
            labels={'x': 'Token', 'y': 'Importance'},
            title="Token-Level Explanation"
        )
        st.plotly_chart(fig)

    if "human_comments" in data.columns:
        st.subheader("Human Comments")
        for comment in data["human_comments"].dropna():
            st.info(comment)
