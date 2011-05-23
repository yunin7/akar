# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from views import NewsListView, NewsDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        NewsListView.as_view(),
        name='news-list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        NewsDetailView.as_view(),
        name='news-detail'
    ),
)
