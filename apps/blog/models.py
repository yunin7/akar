# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from apps.common.models import PostBase, ImageBase
from apps.common.utils import get_first_or_none


class Entry(PostBase):
    u"""модель записи в блоге"""

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

    def image(self):
        get_first_or_none(self.entryimage_set.all())


class EntryImage(ImageBase):
    u"""модель изображения для записи в блоге"""
    entry = models.ForeignKey(Entry)
