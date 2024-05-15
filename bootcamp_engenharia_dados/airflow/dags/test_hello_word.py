
import logging
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger(__name__)

# now = pendulum.now(tz="UTC")
# now_to_the_hour = (now - datetime.timedelta(0, 0, 0, 0, 0, 3)).replace(minute=0, second=0, microsecond=0)
# START_DATE = now_to_the_hour
# DAG_NAME = "test_hello_world"

local_tz = pendulum.timezone("America/Recife")

default_args = {
    'owner': 'Jailton Paiva',
    'depends_on_past': False,
    'email': ['jailtoncarlos@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}


def hello_world():
    print("Hello, World!")
    logger.info(f'>>>>>>hello_world')

with DAG('task_hello_world',
        'Test Task Hello World',
        default_args=default_args,
        schedule_interval='@daily',
        schedule=None, #"*/10 * * * *",
        start_date=pendulum.datetime(2024, 5, 14, tz=local_tz),
        tags=['engdados', 'bootcamp'],
        # template_searchpath=['/opt/airflow/dags/cpa/sqls/']
    ) as dag:

    task_hello = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world,
        dag=dag
    )
