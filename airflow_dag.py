from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

# Default arguments
default_args = {
    'owner': 'saiteja708',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

# Define DAG
dag = DAG(
    'bitcoin_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',   # runs every day
    catchup=False
)

# ✅ Task 1: Extract data
def extract_data():
    subprocess.run(["python", "extract_bitcoin.py"])

# ✅ Task 2: Transform (create charts)
def transform_data():
    subprocess.run(["python", "create_graphs.py"])

# ✅ Task 3: Load to PostgreSQL
def load_data():
    subprocess.run(["python", "load_to_postgres.py"])

# Create tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag
)

# Set task order (pipeline flow)
extract_task >> transform_task >> load_task
