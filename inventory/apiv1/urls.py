from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.api_root, name='apiroot'),

    url(r'users/$', views.UserList().as_view(), name='user-list'),

    # base items
    url(r'baseitems/$', views.BaseItemList().as_view(), name='baseitem-list'),
    url(r'baseitems/create/$', views.BaseItemCreate().as_view(),
        name='baseitem-create'),
    url(r'baseitems/(?P<pk>\d+)/$', views.BaseItemRetrieveUpdateDestroy.as_view(),
        name='baseitem-retrieveupdatedestroy'),

    # items
    url(r'items/$', views.ItemList().as_view(), name='item-list'),
    url(r'items/create/$', views.ItemCreate().as_view(),
        name='item-create'),

    # brands
    url(r'brands/$', views.BrandList().as_view(), name='brand-list'),
    url(r'brands/create/$', views.BrandCreate().as_view(),
        name='brand-create'),

    # categories
    url(r'categories/$', views.CategoryList().as_view(),
        name='category-list'),
    url(r'categories/create/$', views.CategoryCreate().as_view(),
        name='category-create'),

    # locations
    url(r'locations/$', views.LocationList().as_view(),
        name='location-list'),
    url(r'locations/create/$', views.LocationCreate().as_view(),
        name='location-create'),

    # transactions
    url(r'transactions/$', views.TransactionList().as_view(),
        name='transaction-list'),
    url(r'transactions/create/$', views.TransactionCreate().as_view(),
        name='transaction-create'),
]
