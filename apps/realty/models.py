# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models

from apps.common.utils import get_first_or_none
from photologue.models import ImageModel

class ParamModel(models.Model):
    u"""абстрактная модель для моделей параметров"""
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{name}'.format(**self.__dict__)

    @classmethod
    def choices(cls):
        result = [(0, u'Любой')]
        result += cls.objects.values_list('pk', 'name')
        return result


class Town(ParamModel):
    u"""модель параметра город"""

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'

    def get_absolute_url(self):
        return reverse('town-properties', kwargs={'town': self.pk})


class Type(ParamModel):
    u"""модель параметра типа объекта"""

    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Типы объектов'

    def get_absolute_url(self):
        return reverse('type-properties', kwargs={'type': self.pk})


class Property(models.Model):
    u"""модель объекта недвижимости"""
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
    show_on_home = models.BooleanField(verbose_name=u'показывать на главной',
                                    default=False)

    class Meta: 
        ordering = ('-id',)
        verbose_name = u'Объект недвижимости'
        verbose_name_plural = u'Объекты недвижимости'

    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'pk': self.pk})

    def image(self):
        return get_first_or_none(self.propertyimage_set.all())


class PropertyImage(ImageModel):
    u"""модель изображения для объекта недвижимости"""
    property = models.ForeignKey(Property)
    alt = models.CharField(max_length=150, verbose_name=u'описание')