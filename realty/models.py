# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.db import models
from django.contrib import admin 

#Города
class City(models.Model):
    city_name = models.CharField(max_length=150)
    
    class Meta:
	    verbose_name = u'Город'
	    verbose_name_plural = u'Города'

    def __unicode__(self):
        return self.city_name
					  
class CityAdmin(admin.ModelAdmin):
	list_display = ('id', 'city_name')

#Типы объектов
class TypeObject(models.Model):
    city_name = models.CharField(max_length=150)

    class Meta:
	    verbose_name = u'Тип объекта'
	    verbose_name_plural = u'Типы объектов'
    
    def __unicode__(self):
        return self.city_name 

#Объекты недвижимости
class RealObject(models.Model):
    title = models.CharField(max_length=150)
    imagef = models.ForeignKey(City, verbose_name=u'Город')
    real_type = models.ForeignKey(TypeObject, verbose_name=u'Тип объекта')
    price_min = models.IntegerField(verbose_name=u'Минимальная цена')
    price_max = models.IntegerField(verbose_name=u'Максимальная цена')
    timestamp = models.DateTimeField(verbose_name=u'Дата добавления объекта')
    short_text =  models.TextField(verbose_name=u'Краткое описание')
    body = models.TextField(verbose_name=u'Полное описание') 

    class Meta: 
        ordering = ('-id',)
        verbose_name = u'Объект недвижимости'
        verbose_name_plural = u'Объекты недвижимости'


class Gals(models.Model):
  title = models.CharField(max_length=150)
  imagef = models.ForeignKey(RealObject)
  itemgal = models.ImageField(upload_to='objects/')

class GalsInLine(admin.TabularInline):
  model = Gals
  extra = 1
    
class RealObjectAdmin(admin.ModelAdmin):
    fieldsets = [
    (u'Основная информация', {'fields': ['title', 'short_text', 'body']}),(u'Дополнительные параметры',  {'fields': ['real_type', 'imagef', 'price_min','price_max', 'timestamp']}),
    ]
    inlines = [
      GalsInLine,
    ]
  
# Register RealObjects in model admin
admin.site.register(RealObject, RealObjectAdmin) 
admin.site.register(City, CityAdmin) 
admin.site.register(TypeObject, CityAdmin) 

