from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('danhmucs/', views.danhmucs, name='danhmucs'),
    path('danhmuc-edit/<int:id>/', views.danhmuc_edit, name='danhmuc-edit'),
    path('danhmuc-delete/<int:id>/', views.danhmuc_delete, name='danhmuc-delete'),
    path('danhmuc-new/', views.danhmuc_new, name='danhmuc-new'),
    path('khachhangs/', views.khachhangs, name='khachhangs'),
    path('khachhang-edit/<int:id>/', views.khachhang_edit, name='khachhang-edit'),
    path('khachhang-delete/<int:id>/', views.khachhang_delete, name='khachhang-delete'),
    path('khachhang-new/', views.khachhang_new, name='khachhang-new'),
    path('danhmuc-search', views.danhmuc_search, name='danhmuc-search'),
]