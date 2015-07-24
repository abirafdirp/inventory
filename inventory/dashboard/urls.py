from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dashboard.html'),
        name='dashboard'),
    url(r'^base-item-list/$',
        TemplateView.as_view(template_name='partials/base_item_list.html'),
        name='baseitemlist'),
    url(r'^category-list/$',
        TemplateView.as_view(template_name='partials/category_list.html')),
    url(r'^item-list/$',
        TemplateView.as_view(template_name='partials/item_list.html')),
    url(r'^brand-list/$',
        TemplateView.as_view(template_name='partials/brand_list.html')),
    url(r'^transaction-list/$',
        TemplateView.as_view(template_name='partials/transaction_list.html')),
]



