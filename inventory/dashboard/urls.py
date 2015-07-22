from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^base-item-list/$',
        TemplateView.as_view(template_name='partials/base_item_list.html'),
        name='baseitemlist'),
    url(r'^category-list/$',
        TemplateView.as_view(template_name='partials/category_list.html')),
    url(r'^item-list/$',
        TemplateView.as_view(template_name='partials/item_list.html')),
]



