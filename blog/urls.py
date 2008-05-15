# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011
from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
  url(r'^$', 'archive'),
  url(r'^(?P<idblog>\d+)/$', 'blogitem'),
)
