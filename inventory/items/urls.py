from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from items import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'baseitems', views.BaseItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'productidprefixes', views.ProductIdPrefixViewSet)
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'api/baseitem/create/$', views.BaseItemCreate().as_view()),
    url(r'api/item/create/$', views.ItemCreate().as_view()),
]


