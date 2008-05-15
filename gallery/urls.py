# -*- coding: utf-8 -*-
# Gallery application
# (c) Yunin Ivan yunin7@inbox.ru 2011

urlpatterns = patterns('gallery.views',
  url(r'^$', 'gallery'),
  url(r'^(?P<galleryid>\d+)/$', 'gallery_item'),
)
