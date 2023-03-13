import streamlit as st

st.set_page_config(
    page_title="Databricks exam generator",
    page_icon="🎓",
)

col1, col2, col3 = st.columns([2, 3, 2])
col2.image("_static/databricks.png")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown(
    "### Welcome to the Databricks data engineer associate exam generator. Here you can generate exams and test your "
    "knowledge on any theme about data engineering on Databricks."
)
st.markdown("### Select the certification on the sidebar to start.")
