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
    url(r'items/(?P<pk>\d+)/$', views.ItemRetrieveUpdateDestroy.as_view(),
        name='item-retrieveupdatedestroy'),

    # brands
    url(r'brands/$', views.BrandList().as_view(), name='brand-list'),
    url(r'brands/create/$', views.BrandCreate().as_view(),
        name='brand-create'),
    url(r'brands/(?P<pk>\d+)/$', views.BrandRetrieveUpdateDestroy.as_view(),
        name='brand-retrieveupdatedestroy'),

    # categories
    url(r'categories/$', views.CategoryList().as_view(),
        name='category-list'),
    url(r'categories/create/$', views.CategoryCreate().as_view(),
        name='category-create'),
    url(r'categories/(?P<pk>\d+)/$', views.CategoryRetrieveUpdateDestroy.as_view(),
        name='category-retrieveupdatedestroy'),

    # locations
    url(r'locations/$', views.LocationList().as_view(),
        name='location-list'),
    url(r'locations/create/$', views.LocationCreate().as_view(),
        name='location-create'),
    url(r'locations/(?P<pk>\d+)/$', views.LocationRetrieveUpdateDestroy.as_view(),
        name='location-retrieveupdatedestroy'),

    # transactions
    url(r'transactions/$', views.TransactionList().as_view(),
        name='transaction-list'),
    url(r'transactions/create/$', views.TransactionCreate().as_view(),
        name='transaction-create'),
    url(r'transactions/(?P<pk>\d+)/$', views.TransactionRetrieve.as_view(),
        name='transaction-retrieveupdatedestroy'),
]
