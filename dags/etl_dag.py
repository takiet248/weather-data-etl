from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 1),
}

dag = DAG(
    "weather_etl_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,  # Moved here
)

extract_transform = BashOperator(
    task_id="run_pyspark",
    bash_command="python3 /opt/airflow/dags/scripts/etl.py",  # Full path for Docker
    dag=dag,
)

dbt_run = BashOperator(
    task_id="run_dbt",
    bash_command="dbt run --project-dir /opt/airflow/dags/dbt",  # Full path for Docker
    dag=dag,
)

extract_transform >> dbt_run
