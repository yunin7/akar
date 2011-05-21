# -*- coding: utf-8 -*-
# (c) Yunin Ivan yunin7@inbox.ru 2011
from django.db import models


class Gallery(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=u'Корневой раздел')
    title = models.CharField(max_length=150, verbose_name=u'Название раздела')
    alt_text = models.CharField(blank=True, max_length=1000,
                                verbose_name=u'Описание раздела')
    main_foto = models.ImageField(upload_to='gallery/main/')

    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галереи'

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)


class Image(models.Model):
    title = models.CharField(u'Описание', max_length=100)
    gallery = models.ForeignKey(Gallery)
    file = models.ImageField(upload_to='gallery/images/')

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)