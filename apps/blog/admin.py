from django.contrib import admin

from models import EntryImage, Entry


class EntryImages(admin.TabularInline):
    model = EntryImage
    extra = 1


class EntryAdmin(admin.ModelAdmin):
    inlines = [EntryImages,]
    list_display = ('title', 'short_text', 'timestamp')
    list_display_links = ('title', 'short_text')
    
    class Media:
        css = {"all" : ('jwysiwyg/jquery.wysiwyg.css',)}

        js = [
            'js/jquery-1.6.1.min.js',
            'jwysiwyg/jquery.wysiwyg.js',
            'js/admin.js',
        ]


admin.site.register(Entry, EntryAdmin)
