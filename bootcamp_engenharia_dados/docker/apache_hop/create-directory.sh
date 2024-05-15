docker compose down

sudo rm -rf data/server/
mkdir -p data/server/config
mkdir -p data/server/projects/metadata
mkdir -p data/server/projects/files

mkdir -p data/web_ui/config
mkdir -p data/web_ui/projects/metadata
mkdir -p data/web_ui/projects/files
mkdir -p data/web_ui/projects/datasets
mkdir -p data/web_ui/projects/pipelines
mkdir -p data/web_ui/projects/transforms
mkdir -p data/web_ui/projects/workflows

chmod -R 777 data/