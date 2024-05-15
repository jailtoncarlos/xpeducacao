from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from docker.types import Mount


# **LOCAL_PATH_TO_PROJECT_FOLDER** é o caminho para a pasta do projeto no
# sistema de arquivos local (a pasta onde você mantém o arquivo hop-
# config.json, a pasta de metadados e os fluxos de trabalho e pipelines). Esta
# pasta será montada como /project dentro do contêiner.
#
# **LOCAL_PATH_TO_ENV_FOLDER** é semelhante, mas aponta para a pasta onde
# estão os arquivos de configuração do ambiente (JSON). Essa pasta será
# montada como /project-config dentro do contêiner.

# mounts=[Mount(source='LOCAL_PATH_TO_PROJECT_FOLDER', target='/project', type='bind'),
#         Mount(source='LOCAL_PATH_TO_ENV_FOLDER', target='/project-config', type='bind')],



# **Os parâmetros a especificar aqui são:**
# * task_id: um ID exclusivo para essa tarefa de Airflow no DAG.
# * image: usamos "Apache/Hop" neste exemplo, que sempre pegará a
# versão mais recente. Adicione uma tag para usar uma versão
# específica do Apache Hop, por exemplo, "apache/hop:2.6.0" ou
# "apache/hop:Development" para a versão de desenvolvimento mais
# recente.
# * environment é onde informaremos ao DockerOperator qual pipeline
# executar e forneceremos configuração adicional. As variáveis de
# ambiente usadas aqui são exatamente o que você passaria para um
# contêiner autônomo de curta duração sem Airflow:
#
#     HOP_RUN_PARAMETERS: parâmetros a serem passados para
#     fluxo de trabalho ou pipeline.
#
#     HOP_LOG_LEVEL: nível de log a ser usado com seu fluxo de
#     trabalho ou pipeline.
#
#     HOP_FILE_PATH: caminho para o fluxo de trabalho ou pipeline
#     que você deseja usar. Esse é o caminho no contêiner e é
#     relativo à pasta do projeto.
#
#     HOP_PROJECT_DIRECTORY: pasta onde os arquivos de
#     projeto estão salvos. Neste exemplo, esta é a pasta /project que
#     montamos na seção anterior.
#
#     HOP_PROJECT_NAME: nome do projeto Apache Hop. Isso só
#     será usado internamente (e será mostrado nos logs). O nome
#     do seu projeto não é necessariamente o mesmo nome que você
#     usou para desenvolver o projeto no Hop Gui, mas manter as
#     coisas consistentes nunca é demais.
#
#     HOP_ENVIRONMENT_NAME: semelhante ao nome do projeto,
#     esse é o nome do ambiente que será criado por meio do hop-
#     conf quando o contêiner for iniciado.
#
#     HOP_ENVIRONMENT_CONFIG_FILE_NAME_PATHS:
#     caminhos para os arquivos de configuração do ambiente. Esses
#     caminhos de arquivo devem ser relativos à pasta /project-
#     config que montamos na seção anterior.
#
#     HOP_RUN_CONFIG: fluxo de trabalho ou a configuração de
#     execução do pipeline a ser usada. Sua quilometragem pode
#     variar, mas na grande maioria dos casos, usar uma
#     configuração de execução local será o que você precisa.



default_args = {
'owner'                 : 'airflow',
'description'           : 'sample-pipeline',
'depend_on_past'        : False,
'start_date'            : datetime(2022, 1, 1),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 1,
'retry_delay'           : timedelta(minutes=5)
}

with DAG('sample-pipeline', default_args=default_args, schedule_interval=None, catchup=False, is_paused_upon_creation=False) as dag:
    start_dag = DummyOperator(
        task_id='start_dag'
        )

    end_dag = DummyOperator(
        task_id='end_dag'
        )

    hop = DockerOperator(
        task_id='sample-pipeline',
        # use the Apache Hop Docker image. Add your tags here in the default apache/hop: syntax
        image='apache/hop',
        api_version='auto',
        auto_remove=True,
        environment={
            'HOP_RUN_PARAMETERS': 'INPUT_DIR=',
            'HOP_LOG_LEVEL': 'Basic',
            'HOP_FILE_PATH': '${PROJECT_HOME}/transforms/null-if-basic.hpl',
            'HOP_PROJECT_DIRECTORY': '/project',
            'HOP_PROJECT_NAME': 'hop-airflow-sample',
            'HOP_ENVIRONMENT_NAME': 'env-hop-airflow-sample.json',
            'HOP_ENVIRONMENT_CONFIG_FILE_NAME_PATHS': '/project-config/env-hop-airflow-sample.json',
            'HOP_RUN_CONFIG': 'local'
        },

    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[Mount(source='LOCAL_PATH_TO_PROJECT_FOLDER', target='/project', type='bind'),
            Mount(source='LOCAL_PATH_TO_ENV_FOLDER', target='/project-config', type='bind')],
            force_pull=False)

    start_dag >> hop >> end_dag