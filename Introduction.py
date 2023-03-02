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
    "### Welcome to the Databricks exam generator. Here you can generate exams and test your "
    "knowledge on any topic about Databricks."
)
st.markdown("### Select the certification you are interested in on the sidebar to start.")
