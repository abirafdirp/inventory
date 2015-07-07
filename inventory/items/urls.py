from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import
from items import views
urlpatterns = patterns('',
    url(r'api/item/$', views.ItemList.as_view()),
    url(r'api/item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
)


