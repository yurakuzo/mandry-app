#!/bin/bash

# Entry point script for Django application

# Wait for PostgreSQL to start if running in development mode
if [ "$DEBUG" == "True" ]; then
    echo "Running in debug mode. Checking for PostgreSQL readiness..."
    while ! nc -z db 5432; do
        echo "Waiting for PostgreSQL to start..."
        sleep 1  # Increased sleep to reduce log verbosity and system load
    done
    echo "PostgreSQL is ready."
else
    echo "Running in production mode. Skipping PostgreSQL check."
fi

echo "Applying database migrations..."
# Run migrations
python3 manage.py migrate

echo "Collecting static files..."
# Collecting static files, necessary for admin and other static content
python3 manage.py collectstatic --noinput

echo "Starting Django application with Gunicorn..."
# Start Django application using Gunicorn with specified settings
exec gunicorn pet_app.wsgi \
    --worker-class=gevent \
    --worker-connections=1000 \
    --workers=3 \
    --bind 0.0.0.0:5000 \
    --timeout 600
