import sys, site, os
from os.path import join

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)

site.addsitedir(rel('env/lib/python2.6/site-packages'))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, rel('akar'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()