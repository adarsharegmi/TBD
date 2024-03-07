## Setting up db and app

```````docker-compose build
`````` docker-compose up -d

Two environment

PROD and DEVELOPMENT
create .env from sample.env

By default it is using development environment to use docker use

set ENVIRONMENT=PROD


Go inside  docker container to use PROD environment or for testing set DEVELOPMENT as env and create a venv usingn

python -m venv venv
src venv/bin/activate
and install using
pip install -r requirements.txt




##migration
via activated env or inside docker container
alemibic upgrade head
```````
