import os, sys

from django.core.handlers.wsgi import WSGIHandler


sys.stdout = sys.stderr
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()