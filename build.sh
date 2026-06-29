#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd config

python manage.py collectstatic --no-input
python manage.py migrate --no-input

python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if User.objects.filter(username=username).exists():
        print('Superuser ' + username + ' deja present, creation ignoree.')
    else:
        User.objects.create_superuser(username, email, password)
        print('Superuser ' + username + ' cree.')
else:
    print('DJANGO_SUPERUSER_* non definis : creation du superuser ignoree.')
"
