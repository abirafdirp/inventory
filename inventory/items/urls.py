from django.conf.urls import patterns, url, include
from items import views

urlpatterns = [
    url(r'api/$', views.api_root),

    url(r'api/users/$', views.UserList().as_view(),
        name='user-list'),

    # base items
    url(r'api/baseitems/$', views.BaseItemList().as_view(),
        name='baseitem-list'),
    url(r'api/baseitems/create/$', views.BaseItemCreate().as_view(),
        name='baseitem-create'),

    # items
    url(r'api/items/$', views.ItemList().as_view(),
        name='item-list'),
    url(r'api/items/create/$', views.ItemCreate().as_view(),
        name='item-create'),

    # brands
    url(r'api/brands/$', views.BrandList().as_view(),
        name='brand-list'),
    url(r'api/brands/create/$', views.BrandCreate().as_view(),
        name='brand-create'),

    # categories
    url(r'api/categories/$', views.CategoryList().as_view(),
        name='category-list'),
    url(r'api/categories/create/$', views.CategoryCreate().as_view(),
        name='category-create'),

    # product id prefixes
    url(r'api/productidprefixes/$', views.ProductIdPrefixList().as_view(),
        name='productidprefix-list'),
    url(r'api/productidprefixes/create/$',
        views.ProductIdPrefixCreate().as_view(),
        name='productidprefix-create'),

    # locations
    url(r'api/locations/$', views.LocationList().as_view(),
        name='location-list'),
    url(r'api/locations/create/$', views.LocationCreate().as_view(),
        name='location-create'),

    # transactions
    url(r'api/transactions/$', views.TransactionList().as_view(),
        name='transaction-list'),
    url(r'api/transactions/create/$', views.TransactionCreate().as_view(),
        name='transaction-create'),
]


