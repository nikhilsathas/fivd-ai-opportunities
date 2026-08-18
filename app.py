from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


SOURCE_HTML = Path(__file__).with_name("fivd_ai_opportunities.html")

st.set_page_config(
    page_title="Data Centre AI opportunities: priority and fit",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display: none !important;
      }
      .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMain"], .main {
        background: #ffffff;
      }
      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      iframe {
        display: block;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not SOURCE_HTML.exists():
    st.error(f"The presentation file could not be found: {SOURCE_HTML}")
    st.stop()

app_html = SOURCE_HTML.read_text(encoding="utf-8")
app_html = app_html.replace(
    "Generator testing & emissions compliance copilot",
    "Generator Testing & Emissions Compliance Manager",
).replace(
    "Commissioning evidence & anomaly copilot",
    "Commissioning Evidence & Exception Manager",
)

components.html(
    app_html,
    height=2200,
    scrolling=True,
)
