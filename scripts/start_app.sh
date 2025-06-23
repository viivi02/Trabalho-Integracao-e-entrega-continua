#!/bin/bash

docker build -t usuario/app:latest ./app

docker stop app || true
docker rm app || true

docker run -d --name app \
  --network rede_app \
  -p 5000:5000 \
  -e DB_HOST=mysql_app \
  usuario/app:latest
