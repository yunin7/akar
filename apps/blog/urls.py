# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from views import EntryListView, EntryDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        EntryListView.as_view(),
        name='entry-list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        EntryDetailView.as_view(),
        name='entry-detail'
    ),
)
