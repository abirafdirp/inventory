from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'apiv1/$', views.api_root),

    url(r'apiv1/users/$', views.UserList().as_view(),
        name='user-list'),

    # base items
    url(r'apiv1/baseitems/$', views.BaseItemList().as_view(),
        name='baseitem-list'),
    url(r'apiv1/baseitems/create/$', views.BaseItemCreate().as_view(),
        name='baseitem-create'),

    # items
    url(r'apiv1/items/$', views.ItemList().as_view(),
        name='item-list'),
    url(r'apiv1/items/create/$', views.ItemCreate().as_view(),
        name='item-create'),

    # brands
    url(r'apiv1/brands/$', views.BrandList().as_view(),
        name='brand-list'),
    url(r'apiv1/brands/create/$', views.BrandCreate().as_view(),
        name='brand-create'),

    # categories
    url(r'apiv1/categories/$', views.CategoryList().as_view(),
        name='category-list'),
    url(r'apiv1/categories/create/$', views.CategoryCreate().as_view(),
        name='category-create'),

    # product id prefixes
    url(r'apiv1/productidprefixes/$', views.ProductIdPrefixList().as_view(),
        name='productidprefix-list'),
    url(r'apiv1/productidprefixes/create/$',
        views.ProductIdPrefixCreate().as_view(),
        name='productidprefix-create'),

    # locations
    url(r'apiv1/locations/$', views.LocationList().as_view(),
        name='location-list'),
    url(r'apiv1/locations/create/$', views.LocationCreate().as_view(),
        name='location-create'),

    # transactions
    url(r'apiv1/transactions/$', views.TransactionList().as_view(),
        name='transaction-list'),
    url(r'apiv1/transactions/create/$', views.TransactionCreate().as_view(),
        name='transaction-create'),
]
