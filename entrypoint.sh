#!/bin/sh
set -e

echo "Creando migraciones..."
python manage.py makemigrations

echo "Ejecutando migraciones..."
python manage.py migrate --noinput

echo "Creando superusuario..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
import os
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
if username and password and email and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("Superusuario creado")
else:
    print("Superusuario ya existe o faltan variables de entorno")
END

echo "Iniciando servidor Django..."
exec "$@"
