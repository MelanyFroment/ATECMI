import os

import django
from django.contrib.auth import get_user_model

# Must match manage.py / your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        print(f"Création de l'utilisateur {username}...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("L'utilisateur existe déjà.")
else:
    print(
        "Variables manquantes: DJANGO_SUPERUSER_USERNAME et/ou DJANGO_SUPERUSER_PASSWORD. "
        "Aucune création effectuée."
    )
