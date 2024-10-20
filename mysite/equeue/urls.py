from django.urls import path
from . import views

urlpatterns = [
    path('', views.geek_list, name='geek_list'),
]