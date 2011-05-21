# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011
from django.conf.urls.defaults import *

from realty.views import PropertyListView, PropertyDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        PropertyListView.as_view(),
        name='property-list'
    ),
    url(
        r'^town/(?P<town>\d+)/$',
        PropertyListView.as_view(),
        name='town-properties'
    ),
    url(
        r'^type/(?P<type>\d+)/$',
        PropertyListView.as_view(),
        name='type-properties'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        PropertyDetailView.as_view(),
        name='property-detail'
    ),
)
