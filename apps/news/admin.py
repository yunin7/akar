from django.contrib import admin

from models import News, NewsImage


class NewsImages(admin.TabularInline):
    model = NewsImage
    extra = 1
    max_num = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImages,]
    list_display = ('id', 'short_text', 'title', 'timestamp')


admin.site.register(News, NewsAdmin)