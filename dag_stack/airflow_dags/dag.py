from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

# Default settings applied to all tasks
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "catchup": False,
    "start_date": datetime(2021, 1, 1),
}

with DAG(
    dag_id="dag_stack",
    description="An example Airflow DAG running dbt and Great Expectations tasks",
    schedule_interval=None,
    default_args=default_args,
) as dag:
    validate_load = BashOperator(
        task_id="validate_load",
        bash_command="great_expectations --config /root/dag_stack/great_expectations checkpoint run my_checkpoint_01",
    )

    dbt_run = BashOperator(
        task_id="dbt_run", bash_command="dbt run --project-dir /root/dag_stack/dbt"
    )

    validate_load >> dbt_run
