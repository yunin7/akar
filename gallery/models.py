# -*- coding: utf-8 -*-
# (c) Yunin Ivan yunin7@inbox.ru 2011
from django.db import models


class Gallery(models.Model):
    parent = models.ForeignKey(u'self', blank=True, null=True, verbose_name=u'Корневой раздел')
    title = models.CharField(max_length=150, verbose_name=u'Название раздела')
    alt_text = models.CharField(blank=True, max_length=200, verbose_name=u'Описание раздела')
    main_foto = models.ImageField(upload_to='gallery/main/')
    
    def __unicode__(self):
        return u'{title}'.format(**self.__dict__)
