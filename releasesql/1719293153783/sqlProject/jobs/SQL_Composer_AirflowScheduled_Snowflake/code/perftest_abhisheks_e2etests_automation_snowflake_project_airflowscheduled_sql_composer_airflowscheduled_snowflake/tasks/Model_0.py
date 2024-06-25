from perftest_abhisheks_e2etests_automation_snowflake_project_airflowscheduled_sql_composer_airflowscheduled_snowflake.utils import *

def Model_0():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile

    return BashOperator(
        task_id = "Model_0",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/abhisheksr8/scheduledJobs_Snowflake.git",
                 "main"
               )
             ),
             "releasesql/1719293153783/sqlProject"
           ),            "dbt seed --profile run_profile_snowflake",  "dbt run --profile run_profile_snowflake",            "dbt test --profile run_profile_snowflake"]
        ),
        env = {
          "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
          "DBT_PROFILES_DIR": "/home/airflow/gcs/data", 
          "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
          "DBT_FULL_REFRESH": "true"
        },
        append_env = True,
    )
