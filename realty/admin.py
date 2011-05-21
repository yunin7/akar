# -*- coding: utf-8 -*-
from django.contrib import admin
from realty.models import Image, Property, Town, Type


class GalsInLine(admin.TabularInline):
    model = Image
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
                'timestamp'
            ]}
        ),
    ]
    inlines = [GalsInLine,]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Town)
admin.site.register(Type)

