from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import *

# https://docs.djangoproject.com/en/1.10/topics/http/urls/

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^task/$', TaskView.as_view()),
    url(r'^task/(?P<id>[a-z0-9-]+)/$', TaskResultView.as_view()),
    url(r'^list/', ListView.as_view()),
    url(r'^detail/?', DetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
