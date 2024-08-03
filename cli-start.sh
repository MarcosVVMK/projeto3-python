#!/bin/sh

# Tentar subir os contêineres com 'docker compose'
docker compose up -d; 

# Anexar ao contêiner cli-app
docker attach cli-app