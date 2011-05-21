# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from managers import TypeManager, TownManager


class Town(models.Model):
    u'модель города'
    name = models.CharField(max_length=150)
    objects = TownManager()
    
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'

    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)

    def get_absolute_url(self):
        return reverse('town-properties', kwargs={'type': self.pk})

class Type(models.Model):
    u'модель типа объекта'
    name = models.CharField(max_length=150)
    objects = TypeManager()

    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Типы объектов'
    
    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)

    def get_absolute_url(self):
        return reverse('type-properties', kwargs={'type': self.pk})


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