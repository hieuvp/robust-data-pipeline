from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

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
        dag_id='airflow_demo_dag',
        description='An example Airflow DAG',
        schedule_interval=None,
        default_args=default_args
) as dag:
    t0 = BashOperator(
        task_id='bash_task_0',
        bash_command='echo "Hi there, this is the first Airflow task!"'
    )

    t1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo "Sleeping..." && sleep 5s && date'
    )

    t0 >> t1
