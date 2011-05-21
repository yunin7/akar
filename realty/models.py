# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011
from datetime import datetime

from django.db import models


class City(models.Model):
    u'модель города'
    name = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'

    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)


class TypeObject(models.Model):
    u'модель типа объекта'
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Типы объектов'
    
    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)


class Property(models.Model):
    u'модель объекта недвижимости'
    title = models.CharField(max_length=150)
    imagef = models.ForeignKey(City, verbose_name=u'Город')
    real_type = models.ForeignKey(TypeObject, verbose_name=u'Тип объекта')
    price_min = models.IntegerField(verbose_name=u'Минимальная цена')
    price_max = models.IntegerField(verbose_name=u'Максимальная цена')
    timestamp = models.DateTimeField(verbose_name=u'Дата добавления объекта', default=datetime.now())
    short_text =  models.TextField(verbose_name=u'Краткое описание')
    body = models.TextField(verbose_name=u'Полное описание') 

    class Meta: 
        ordering = ('-id',)
        verbose_name = u'Объект недвижимости'
        verbose_name_plural = u'Объекты недвижимости'

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)


class Image(models.Model):
    u'модель изображения для объекта недвижимости'
    title = models.CharField(max_length=150)
    property = models.ForeignKey(Property)
    file = models.ImageField(upload_to='objects/')

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)