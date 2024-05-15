# Defina o argumento para a imagem base
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

USER root

# Cria um novo usuário e grupo com UID e GID especificados
ARG USER_ID
ARG GROUP_ID
RUN if ! getent group ${GROUP_ID} ; then addgroup --gid ${GROUP_ID} hopgroup ; fi && \
    if ! getent passwd ${USER_ID} ; then adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} hopuser ; fi

# Cria os diretórios necessários
RUN mkdir -p /hop/projects/metadata \
    && mkdir -p /hop/projects/files \
    && mkdir -p /hop/projects/datasets \
    && mkdir -p /hop/projects/pipelines \
    && mkdir -p /hop/projects/transforms \
    && mkdir -p /hop/projects/workflows

# Verifica a existência do diretório antes de ajustar permissões
RUN if [ -d /usr/local/tomcat ]; then chown -R ${USER_ID}:${GROUP_ID} /usr/local/tomcat && chmod -R 775 /usr/local/tomcat; fi

# Copia o script de entrada e ajusta suas permissões
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Ajusta as permissões dos diretórios para o usuário criado
RUN chown -R ${USER_ID}:${GROUP_ID} /hop/projects

USER ${USER_ID}

ENTRYPOINT ["/entrypoint.sh"]

# O comando padrão será sobrescrito pelo docker-compose.yml
CMD ["/bin/sh"]
