import pytest
from unittest.mock import patch
import sys
sys.path.append("..")
from utils.loader import load_data


@pytest.fixture
def mock_data():
    data = {
        "data_transform_data_with_spark_sql": {},
        "data_transform_data_with_pyspark": {},
        "data_manage_data_with_delta_lake": {},
        "data_manage_data_access_with_unity_catalog": {},
        "data_build_data_pipeline_with_DLT_spark_sql": {},
        "data_build_data_pipeline_with_DLT_pyspark": {},
        "data_get_started_with_databricks_workspace": {},
        "data_deploy_workloads_with_databricks_workflows": {},
    }
    return data


def test_load_data_cache(mock_data):
    with patch('json.load', return_value={}):
        data_1 = load_data("Data engineer Associate")
        data_2 = load_data("Data engineer Associate")

    assert data_1 == mock_data
    assert data_2 == mock_data