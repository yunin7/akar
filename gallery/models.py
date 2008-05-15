# -*- coding: utf-8 -*-
# Gallery application
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.db import models
from django.contrib import admin 

class RazdelGallery(models.Model):
    parent = models.ForeignKey(u'self', blank=True, null=True, verbose_name=u'Корневой раздел')
    title = models.CharField(max_length=150, verbose_name=u'Название раздела')
    alt_text = models.CharField(blank=True, max_length=200, verbose_name=u'Описание раздела')
    main_foto = models.ImageField(upload_to='gallery/main/')
    
    def __unicode__(self):
        return self.title
    
class RazdelGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'alt_text', 'main_foto')
    
admin.site.register(RazdelGallery, RazdelGalleryAdmin)
