from django.contrib import admin

from .models import Gallery


class RazdelGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'alt_text', 'main_foto')

admin.site.register(Gallery, RazdelGalleryAdmin)
