import json
import streamlit as st


@st.cache_data
def load_data(exam):
    """
        Load exam questions data from JSON files and return as a dictionary.

        Parameters:
        -----------
        exam: str
            The name of the exam to load data for.

        Returns:
        --------
        data: dict
            A dictionary containing the loaded exam data.
        """
    if exam == "Data engineer Associate":
        with open("questions/build_data_pipeline_with_DLT_pyspark.json") as json_file:
            data_build_data_pipeline_with_dlt_pyspark = json.load(json_file)
        with open("questions/build_data_pipeline_with_DLT_spark_sql.json") as json_file:
            data_build_data_pipeline_with_dlt_spark_sql = json.load(json_file)
        with open("questions/deploy_workloads_with_databricks_workflows.json") as json_file:
            data_deploy_workloads_with_databricks_workflows = json.load(json_file)
        with open("questions/get_started_with_databricks_workspace.json") as json_file:
            data_get_started_with_databricks_workspace = json.load(json_file)
        with open("questions/manage_data_access_with_unity_catalog.json") as json_file:
            data_manage_data_access_with_unity_catalog = json.load(json_file)
        with open("questions/manage_data_with_delta_lake.json") as json_file:
            data_manage_data_with_delta_lake = json.load(json_file)
        with open("questions/transform_data_with_pyspark.json") as json_file:
            data_transform_data_with_pyspark = json.load(json_file)
        with open("questions/transform_data_with_spark_sql.json") as json_file:
            data_transform_data_with_spark_sql = json.load(json_file)
        data = {
            "data_transform_data_with_spark_sql": data_transform_data_with_spark_sql,
            "data_transform_data_with_pyspark": data_transform_data_with_pyspark,
            "data_manage_data_with_delta_lake": data_manage_data_with_delta_lake,
            "data_manage_data_access_with_unity_catalog": data_manage_data_access_with_unity_catalog,
            "data_build_data_pipeline_with_DLT_spark_sql": data_build_data_pipeline_with_dlt_spark_sql,
            "data_build_data_pipeline_with_DLT_pyspark": data_build_data_pipeline_with_dlt_pyspark,
            "data_get_started_with_databricks_workspace": data_get_started_with_databricks_workspace,
            "data_deploy_workloads_with_databricks_workflows": data_deploy_workloads_with_databricks_workflows,
        }
    return data
