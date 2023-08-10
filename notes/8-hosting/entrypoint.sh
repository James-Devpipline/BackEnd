#! /bin/bash

pipenv run gunicorn app:app --config gunicorn_config.py app:app
# first app is app.py, second is the app = init in app.py

# docker run --name add-auth-model -e DATABASE_PRE="postgresql://" -e DATABASE_USER="james" -e DATABASE_ADDR="127.0.0.1" -e DATABASE_PORT="8432" -e DATABASE_NAME="marshmallow" -e DATABASE_PASS="12345678" -d -p 8000:8000 8-hosting:latest