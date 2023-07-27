from airflow import DAG
from airflow.operators.dummy import DummyOperator

from datetime import datetime

# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2021, 1, 1)
}

with DAG(
    dag_id='dag_stack',
    description='An example Airflow DAG running dbt and Great Expectations tasks',
    schedule_interval=None,
    default_args=default_args
    ) as dag:

    t0 = DummyOperator(task_id='dummy_task')
