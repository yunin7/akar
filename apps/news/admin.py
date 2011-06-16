from django.contrib import admin

from models import News, NewsImage


class NewsImages(admin.TabularInline):
    model = NewsImage
    extra = 1
    max_num = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImages,]
    list_display = ('id', 'short_text', 'title', 'timestamp')

    class Media:
        css = {"all" : ('jwysiwyg/jquery.wysiwyg.css',)}

        js = [
            'js/jquery-1.6.1.min.js',
            'js/admin.js',
            'jwysiwyg/jquery.wysiwyg.js',
        ]

admin.site.register(News, NewsAdmin)