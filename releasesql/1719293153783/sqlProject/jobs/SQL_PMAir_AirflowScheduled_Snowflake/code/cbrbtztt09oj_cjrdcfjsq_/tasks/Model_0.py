from cbrbtztt09oj_cjrdcfjsq_.utils import *

def Model_0():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile

    return BashOperator(
        task_id = "Model_0",
        bash_command = f'''$PROPHECY_HOME/run_dbt.sh "{"; ".join(["dbt seed --profile run_profile", "dbt run --profile run_profile", "dbt test --profile run_profile"])}"''',
        env = {
          "DBT_DATABRICKS_INVOCATION_ENV": "prophecy", 
          "DBT_SEND_ANONYMOUS_USAGE_STATS": "false", 
          "DBT_FULL_REFRESH": "true", 
          "DBT_PROFILE_SECRET": "uS3wuk1ILFzh5fEJxTlXW", 
          "GIT_TOKEN_SECRET": "DXruqNOd9IYCMFlSzeENvg_", 
          "GIT_ENTITY": "branch", 
          "GIT_ENTITY_VALUE": "main", 
          "GIT_SSH_URL": "https://github.com/abhisheksr8/scheduledJobs_Snowflake.git", 
          "GIT_SUB_PATH": "releasesql/1719293153783/sqlProject", 
          "IS_ADHOC_RUN_FROM_SAME_PROJECT": "false"
        },
        append_env = True,
    )
