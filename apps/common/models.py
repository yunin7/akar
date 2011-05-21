# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models


class PostBase(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'Заголовок')
    short_text =  models.TextField(u'краткое описание')
    body = models.TextField(u'полное описание')
    timestamp = models.DateTimeField(default=datetime.now())

    class Meta:
        abstract = True
        ordering = ('-timestamp',)

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)