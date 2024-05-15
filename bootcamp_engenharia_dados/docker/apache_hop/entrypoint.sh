#!/bin/bash

# Ajusta as permissões dos diretórios
chown -R hopuser:hopgroup /hop

# Ajusta as permissões dos diretórios antes de iniciar o servidor
chown -R hopuser:hopgroup /usr/local/tomcat

# Executa o comando como o usuário especificado
exec "$@"
