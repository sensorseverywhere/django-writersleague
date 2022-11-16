#!/usr/bin/env bash

cd /home/miriad/writersleague

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --no-input
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsu
 
