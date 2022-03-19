from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_info', views.add_info, name='add_info')
]