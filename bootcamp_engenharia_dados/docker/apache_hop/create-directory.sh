docker compose down

sudo rm -rf data/server/
mkdir -p data/server/config
mkdir -p data/server/projects/metadata
mkdir -p data/server/projects/files

mkdir -p data/web_ui/config
mkdir -p data/web_ui/projects/metadata
mkdir -p data/web_ui/projects/files

chmod -R 777 data/