# django-starter
Boilerplate Django project

## Getting started

1) Configure [Docker](https://docs.docker.com/)
2) Run Docker Compose: `docker-compose up`

## Scripts

- **manage.sh**: Execute Django *manage.py* commands. E.g: `./scripts/manage.sh DJANGO_COMMAND`

## Docker Commands
Build and Run
- `docker-compose build --build-arg APP_ENVIROMENT="develop"`
- `docker-compose up`
- `docker-compose down`
- `docker exec -it IMAGE_ID sh`


Exec commands in Services
- `docker-compose exec db psql --username={{username}} --dbname={{dbname}}`
- `docker-compose exec web python src/manage.py createsuperuser`


## Django Commands
- `py.test`


## Without Docker
```
- python3.8 -m venv venv
source venv/bin/activate
- python manage.py migrate
- python manage.py runserver
```

## Links interessantes

- [Dockerizing Django](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
- [Makefile Django](https://dev.to/xarala221/how-to-become-more-productive-using-makefile-579b/)