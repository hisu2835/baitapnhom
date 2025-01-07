from django.urls import path
from . import views

urlpatterns = [
    path('webbs/', views.Customer, name='webbs'),
    path('webbs/', views.Category, name='webbs'),
    path('webbs/', views.Product, name='webbs'),
    path('webbs/', views.Order, name='webbs'),
    path('webbs/', views.OrderItem, name='webbs'),
    path('webbs/', views.Cart, name='webbs'),
    path('webbs/', views.CartItem, name='webbs'),
]