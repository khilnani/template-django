from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from sample.views import *

urlpatterns = patterns('',
    url(r'^list/', ListView.as_view()),
    url(r'^detail/?', DetailView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

