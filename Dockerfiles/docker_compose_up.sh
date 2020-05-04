#!/bin/sh

docker stop $(docker ps -q)
docker rm $(docker ps -q -a)
# docker rmi $(docker images -q) -f

rsync -av --exclude=app/tests* app Dockerfiles/app

docker-compose -f Dockerfiles/app/docker-compose.yml up --build
