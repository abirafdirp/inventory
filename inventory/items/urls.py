from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from items import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'baseitems', views.BaseItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'brands', views.BrandViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]


