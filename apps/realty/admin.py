# -*- coding: utf-8 -*-
from django.contrib import admin

from models import PropertyImage, Property, Town, Type


class PropertyImages(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Основная информация', {'fields':['title', 'short_text', 'body']}),
        (u'Дополнительные параметры',
            {'fields':[
                'type',
                'town',
                'price_min',
                'price_max',
                'square_min',
                'square_max',
                'timestamp',
                'show_on_home'
            ]}
        ),
    ]
    inlines = [PropertyImages,]

    class Media:
        css = {"all" : ('jwysiwyg/jquery.wysiwyg.css',)}

        js = [
            'js/jquery-1.6.1.min.js',
            'js/admin.js',
            'jwysiwyg/jquery.wysiwyg.js',
        ]

admin.site.register(Property, PropertyAdmin)
admin.site.register(Town)
admin.site.register(Type)

