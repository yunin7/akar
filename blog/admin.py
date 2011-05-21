from django.contrib import admin

from .models import Image, Entry


class GalsInLine(admin.TabularInline):
    model = Image
    extra = 1


class EntryAdmin(admin.ModelAdmin):
    inlines = [GalsInLine,]
    list_display = ('title', 'short_text', 'timestamp')
    list_display_links = ('title', 'short_text')


admin.site.register(Entry, EntryAdmin)
