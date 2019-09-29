docker-compose build
docker-compose up -d
docker-compose run web python manage.py migrate --noinput