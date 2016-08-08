from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^scans/$', views.scan_list),
    url(r'^scans/(?P<pk>[0-9]+)/$', views.scan_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
