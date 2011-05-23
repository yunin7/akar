# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from views import GalleryListView, GalleryDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        GalleryListView.as_view(),
        name='gallery-list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        GalleryDetailView.as_view(),
        name='gallery-detail'
    ),
)
