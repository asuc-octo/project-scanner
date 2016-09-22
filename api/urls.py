from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^scans/$', views.ScanList.as_view()),
    url(r'^scans/(?P<pk>[0-9]+)/$', views.ScanDetail.as_view()),
    url(r'^scanners/$', views.ScannerList.as_view()),
    url(r'^scanners/(?P<pk>[0-9]+)/$', views.ScannerDetail.as_view()),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]