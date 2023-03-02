import streamlit as st
from config import settings
from utils.loader import load_data
from utils.exam import display_question,pick_randomized_questions, generate_full_exam, get_answers, get_results, table_results

data = load_data("Data engineer Associate")

st.sidebar.write("You can generate a new exam from here. "
                 "Notice that the default number of questions for each topic is the default number in the actual exam.")

db_lakehouse_nbq = st.sidebar.slider('Databricks Lakehouse Platform', 0, 25, settings.get_started_with_databricks_workspace_nb_questions, key=1)
manage_data_delta_lake_nbq = st.sidebar.slider('Manage data with Delta Lake', 0, 25, settings.manage_data_with_delta_lake_nb_questions, key=2)
elt_spark_sql_nbq = st.sidebar.slider('ELT with Spark SQL', 0, 25, settings.build_data_pipeline_with_DLT_spark_sql_nb_questions, key=3)
elt_spark_pyspark_nbq =  st.sidebar.slider('ELT with PySpark', 0, 25, settings.build_data_pipeline_with_DLT_pyspark_nb_questions, key=4)
transform_data_spark_sql_nbq = st.sidebar.slider('Transform data with Spark SQL', 0, 25, settings.transform_data_with_spark_sql_nb_questions, key=5)
transform_data_pyspark_nbq = st.sidebar.slider('Transform data with PySpark', 0, 25, settings.transform_data_with_pyspark_nb_questions, key=6)
production_pipelines_nbq = st.sidebar.slider('Production Pipelines', 0, 25, settings.deploy_workloads_with_databricks_workflows_nb_questions, key=7)
data_governance_nbq = st.sidebar.slider('Data Governance', 0, 25, settings.manage_data_access_with_unity_catalog_nb_questions, key=8)
nb_questions = [transform_data_spark_sql_nbq, transform_data_pyspark_nbq, manage_data_delta_lake_nbq, data_governance_nbq, elt_spark_sql_nbq, elt_spark_pyspark_nbq, db_lakehouse_nbq, production_pipelines_nbq]
st.sidebar.markdown("### Questions: " + str(sum(nb_questions)))
if st.sidebar.button("Generate exam"):
    st.session_state['exam_questions'] = pick_randomized_questions(data, nb_questions)

if 'exam' not in st.session_state:
    st.session_state['exam'] = ""
    st.session_state['exam_questions'] = ""

try:
    form = st.form("exam_form")
    answers_dic = {}
    st.session_state['exam'] = generate_full_exam(st.session_state['exam_questions'], form, answers_dic)
    if form.form_submit_button("Submit"):
        answers = get_answers(st.session_state['exam_questions'])
        count_true, perc_true, results = get_results(answers, st.session_state['exam'])
        st.markdown("")
        st.markdown("")
        st.markdown("")
        col1, col2, col3, col4 = st.columns([1,3,4,1])
        col3.markdown("")
        col3.markdown("")
        col3.markdown("")
        col3.markdown("")
        col2.markdown("# " + str(count_true) + "/" + str(len(answers)))
        col2.markdown("# " + str(perc_true) + "%")
        if perc_true >= 70:
            col3.write("Congratulations, you would have passed this exam! You might be ready to go for the real one!")
        else:
            col3.write("You failed the exam but keep on working and you will be ready soon! 💪")
        st.markdown("")
        st.markdown("")
        cola, colb, colc = st.columns([3,2,3])
        colb.write(table_results(results))
except:
    st.write("Select the number of questions for each topic and click the __Generate exam__ button on the sidebar to start.")