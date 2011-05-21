# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011
from django.conf.urls.defaults import patterns, url

from views import GalleryListView, GalleryDetailView


urlpatterns = patterns('',
    url(r'^$', GalleryListView.as_view(), name='gallery-list'),
    url(r'^(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery-detail'),
)
