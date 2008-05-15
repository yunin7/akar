# -*- coding: utf-8 -*-
# News application
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
  url(r'^$', 'newsarchive'),
)
