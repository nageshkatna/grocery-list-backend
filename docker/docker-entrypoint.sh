#!/bin/bash
set -e

echo "Waiting for database at $DATABASE_HOST:$DATABASE_PORT..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.5
done

echo "Running tests..."
python manage.py test api.tests

echo "Running migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT