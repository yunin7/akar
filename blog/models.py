# -*- coding: utf-8 -*-
from django.db import models

from common.models import PostBase


class Entry(PostBase):
    logo = models.ImageField(upload_to='blog/logos/')
    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

class Image(models.Model):
    title = models.CharField(max_length=150)
    entry = models.ForeignKey(Entry)
    file = models.ImageField(upload_to='blog/images/')
