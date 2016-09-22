from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', RedirectView.as_view(pattern_name='scannerlist')),
    url(r'^scans/$', views.ScanList.as_view(),name='scanlist'),
    url(r'^scans/(?P<pk>[0-9]+)/$', views.ScanDetail.as_view(),name='scandetail'),
    url(r'^scanners/$', views.ScannerList.as_view(), name='scannerlist'),
    url(r'^scanners/(?P<pk>[0-9]+)/$', views.ScannerDetail.as_view(),name='scannerdetail'),
    url(r'^locations/$', views.LocationList.as_view(),name='locationlist'),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view(),name='locationdetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]