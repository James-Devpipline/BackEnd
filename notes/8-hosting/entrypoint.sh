#! /bin/bash

pipenv run gunicorn app:app
# first app is app.py, second is the app = init in app.py