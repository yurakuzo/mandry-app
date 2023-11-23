#!/bin/sh

# Wait for postgresql to start
while ! nc -z db 5432; do
    echo "Waiting for postrges to start..."
    sleep 0.1
done

# Run migrations
python3 manage.py migrate

# Collecting static files, at least for admin page
python3 manage.py collectstatic --noinput

echo "Creating superuser $ADMIN_lOGIN"
python manage.py createsuperuser --no-input --username $ADMIN_USER --email $ADMIN_USER@example.com
echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='$ADMIN_USER'); user.set_password('$ADMIN_PASSWORD'); user.save()" | python manage.py shell

exec gunicorn -b :$APP_PORT -b :2222 mandry.wsgi --reload