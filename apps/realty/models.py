# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from managers import TypeManager, TownManager


class ParamModel(models.Model):
    name = models.CharField(max_length=150)
    url_name = ''

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)

    def get_absolute_url(self):
        return reverse(self.url_name, kwargs={'type': self.pk})

    @classmethod
    def choices(cls):
        result = [(0, u'Любой')]
        result += cls.objects.values_list('pk', 'name')
        return result


class Town(ParamModel):
    u'модель города'
    url_name = 'town-properties'

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'


class Type(ParamModel):
    u'модель типа объекта'
    url_name = 'type-properties'

    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Типы объектов'


class Property(models.Model):
    u'модель объекта недвижимости'
    title = models.CharField(max_length=150)
    town = models.ForeignKey(Town, verbose_name=u'Город')
    type = models.ForeignKey(Type, verbose_name=u'Тип объекта')
    price_min = models.IntegerField(verbose_name=u'Минимальная цена')
    price_max = models.IntegerField(verbose_name=u'Максимальная цена')
    square_min = models.IntegerField(verbose_name=u'Минимальная площадь')
    square_max = models.IntegerField(verbose_name=u'Максимальная площадь')
    timestamp = models.DateTimeField(verbose_name=u'Дата добавления объекта',
                                     default=datetime.now())
    short_text =  models.TextField(verbose_name=u'Краткое описание')
    body = models.TextField(verbose_name=u'Полное описание') 

    class Meta: 
        ordering = ('-id',)
        verbose_name = u'Объект недвижимости'
        verbose_name_plural = u'Объекты недвижимости'

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'pk': self.pk})


class Image(models.Model):
    u'модель изображения для объекта недвижимости'
    title = models.CharField(max_length=150)
    property = models.ForeignKey(Property)
    file = models.ImageField(upload_to='objects/')

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)