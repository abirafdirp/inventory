from django.conf.urls import url
from . import views

urlpatters = [
    url(r'^&', views.DashboardView().as_view(), name='dashboard'),
]



