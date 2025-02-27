"""
URL configuration for web_ban_hang_bim_sua project.

The `urlpatterns` list routes URLs to views. For more information please see:
    path('shop/', include('core.urls')),  # Thêm đường dẫn từ core
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    path('shop/', include('core.urls')),  # Thêm đường dẫn từ core
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    path('shop/', include('core.urls')),  # Thêm đường dẫn từ core
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    path('shop/', include('core.urls')),  # Thêm đường dẫn từ core
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_from_key.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_from_key_done.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # core xử lý trang chính, bao gồm login
    path('webbs/', include('webbs.urls')),
    path('home/', include('home.urls')),
]
