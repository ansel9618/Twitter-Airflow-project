from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl
from airflow.operators.email_operator import EmailOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# dag = DAG(
#     'twitter_dag',
#     default_args=default_args,
#     description='Our first DAG with ETL process!',
#     schedule_interval=timedelta(days=1),
# )

dag = DAG(
    dag_id='twitter_dag',
    default_args=default_args,
    description='My first etl code',
    start_date = days_ago(1)
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)


success_notify = EmailOperator(
    task_id='sucess_email_notify',
    to='gowk510@gmail.com',
    subject='Pipeline Execution Success',
    html_content=""" <h1>Great job :) tweets has been pushed to s3.</h1> """,
    trigger_rule='all_success',
    dag=dag
)

failure_notify = EmailOperator(
    task_id='failure_email_notify',
    to='gowk510@gmail.com',
    subject='Pipeline Execution failed',
    html_content=""" <h1>Sorry :( Failed to load tweets into s3 .</h1> """,
    trigger_rule='all_failed',
    dag=dag
)

run_etl >> [success_notify,failure_notify]