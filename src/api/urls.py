from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^sample/',include('sample.urls')),
    url(r'help/?', include('rest_framework_swagger.urls')),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
