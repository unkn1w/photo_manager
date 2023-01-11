#!/bin/bash
python /src/backend/manage.py wait_for_db
python /src/backend/manage.py migrate
python /src/backend/manage.py runserver 0.0.0.0:8000
