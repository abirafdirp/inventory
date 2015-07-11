from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from items import views



urlpatterns = [
    # url(r'api/$', views.APIRootView.as_view()),
    url(r'api/users/$', views.UserList().as_view()),
    url(r'api/baseitems/$', views.BaseItemList().as_view()),
    url(r'api/baseitems/create/$', views.BaseItemCreate().as_view()),
    url(r'api/items/$', views.ItemList().as_view()),
    url(r'api/items/create/$', views.ItemCreate().as_view()),
    url(r'api/brands/$', views.BrandList().as_view()),
    url(r'api/brands/create/$', views.BrandCreate().as_view()),
    url(r'api/categories/$', views.CategoryList().as_view()),
    url(r'api/categories/create/$', views.CategoryCreate().as_view()),
    url(r'api/productidprefixes/$', views.ProductIdPrefixList().as_view()),
    url(r'api/productidprefixes/create/$',
        views.ProductIdPrefixCreate().as_view()),
    url(r'api/locations/$', views.LocationList().as_view()),
    url(r'api/locations/create/$', views.LocationCreate().as_view()),
    url(r'api/transactions/$', views.TransactionList().as_view()),
    url(r'api/transactions/create/$', views.TransactionCreate().as_view()),
]


