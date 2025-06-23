#!/bin/bash

docker network create rede_app || true

docker run -d --name mysql_app \
  --network rede_app \
  -e MYSQL_ROOT_PASSWORD=senha \
  -e MYSQL_DATABASE=meubanco \
  -p 3308:3306 \
  mysql:8.0

echo "Aguardando o MySQL iniciar..."
sleep 20

docker exec -i mysql_app mysql -uroot -psenha meubanco <<EOF
CREATE TABLE IF NOT EXISTS pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);
EOF
