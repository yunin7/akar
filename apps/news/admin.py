from django.contrib import admin

from models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text', 'title', 'timestamp')


admin.site.register(News, NewsAdmin)