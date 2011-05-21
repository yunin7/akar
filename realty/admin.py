# -*- coding: utf-8 -*-
from django.contrib import admin
from realty.models import Image, Property, City, TypeObject


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name')


class GalsInLine(admin.TabularInline):
    model = Image
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Основная информация', {'fields':['title', 'short_text', 'body']}),
        (u'Дополнительные параметры', {'fields':
             ['real_type', 'imagef', 'price_min','price_max', 'timestamp']}
        ),
    ]
    inlines = [GalsInLine,]

# Register RealObjects in model admin
admin.site.register(Property, PropertyAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(TypeObject, CityAdmin)

