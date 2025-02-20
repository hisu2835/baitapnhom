from django.urls import path,include
from . import views
from django.contrib import admin

app_name = 'webbs'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')), 
]