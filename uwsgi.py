import os, sys

from django.core.handlers.wsgi import WSGIHandler


sys.path.insert(0, '/usr/local/www/akar')
sys.stdout = sys.stderr
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()