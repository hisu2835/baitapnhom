from django.urls import path
from . import views

app_name = 'webbs'

urlpatterns = [
    path('', views.home, name='home'),
]