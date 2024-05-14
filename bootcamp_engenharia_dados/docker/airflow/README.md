# Sobre

Repositório com os arquivos necessários para ter uma instância do Airflow em ambiente local.

Repositório base: https://git.lais.huol.ufrn.br/infra/gitops/spark-dev/airflow

## Instruções

Crie um arquivo .env a partir do .env_sample. Adicione as dependências Python necessárias na variável de ambiente `_PIP_ADDITIONAL_REQUIREMENTS`.

Utilize os arquivos `*.sh` para:
- `bash.sh`: Acessar o CLI do container de aplicação, possibilitando rodar teste de `dags` e `tasks`.
- `clear.sh`: Remova todos os containers do projeto.
- `up.sh`: Suba os containers do projeto.

# Importante!

Ao subir os containers, na estrutura atual, a pasta `./dags` será criada. Coloque nessa pasta todas as _dags_ que for trabalhar. Se fizer parte de algum projeto que já tenha _dags_, clone o repositório para dentro da pasta `./dags`.

Sempre que tiver dúvida, pergunte!
