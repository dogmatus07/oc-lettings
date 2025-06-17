#!/bin/bash
# This script is used to run the Django application with Gunicorn
python manage.py migrate --noinput
python load_fixtures.py
python manage.py collectstatic --noinput
exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
