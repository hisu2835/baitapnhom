from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('danh-muc/', views.danh_muc, name='danh_muc'),
    path('edit-danh-muc/', views.edit_danh_muc, name='edit_danh_muc'),
]