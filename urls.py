from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^properties/', include('apps.realty.urls')),
	(r'^blog/', include('apps.blog.urls')),
	(r'^news/', include('apps.news.urls')),
#	(r'^accounts/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^feedback/', include('feedback.urls')),
    (r'^', include('photologue.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
