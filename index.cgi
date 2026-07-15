#!/usr/bin/python3
import os
import sys

# On indique à Python où se trouvent les fichiers du projet
sys.path.insert(0, '/home/sutrbml/www')

# Configuration de la variable d'environnement pour Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Import et lancement de l'application WSGI
from django.core.handlers.wsgi import WSGIHandler
from wsgiref.handlers import CGIHandler

class CGIHandlerCustom(CGIHandler):
    # Correction pour s'assurer que les en-têtes passent bien sur OVH
    def read_environ(self):
        super().read_environ()
        if 'HTTP_AUTHORIZATION' in os.environ:
            self.environ['HTTP_AUTHORIZATION'] = os.environ['HTTP_AUTHORIZATION']

if __name__ == '__main__':
    CGIHandlerCustom().run(WSGIHandler()) 