from regression_abhisheks_e2etests_automation_snowflake_project_airflowscheduled_sql_composer_airflowscheduled_snowflake.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "6963",
          "git_entity": "branch",
          "git_entity_value": "main",
          "git_ssh_url": "https://github.com/abhisheksr8/scheduledJobs_Snowflake.git",
          "git_sub_path": "releasesql/1734544062319/sqlProject",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile_snowflake",
          "envs": {
            "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
            "DBT_PROFILES_DIR": "/home/airflow/gcs/data", 
            "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
            "DBT_FULL_REFRESH": "true"
          }
        },
    )
