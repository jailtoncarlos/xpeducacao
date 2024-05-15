#!/bin/bash

# Ajusta as permissões dos diretórios
chown -R hopuser:hopgroup /hop

# Executa o comando como o usuário especificado
exec gosu hopuser:hopgroup "$@"
