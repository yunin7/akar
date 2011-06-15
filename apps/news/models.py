# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from apps.common.models import PostBase, ImageBase


class News(PostBase):
    u"""модель новости"""
#    logo = models.ImageField(upload_to='news/logos/')

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def image(self):
        return self.newsimage


class NewsImage(ImageBase):
    u"""модель изображения для новости"""
    entry = models.OneToOneField(News)