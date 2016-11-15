"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

admin.autodiscover()
schema_view = get_swagger_view()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/?', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('{{ project_name }}.apps.api.urls')),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
