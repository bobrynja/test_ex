"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wallet import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile),
    path('accounts/profile/add/', views.add),
    path('accounts/profile/add/create/', views.create_w),
    path('accounts/profile/transfer/', views.transfer), 
    path('users/', views.user),
    path('wallets/', views.wallet),
    path('users/wallets/', views.wallet),
    path('api/', include('wallet.urls')),
]
