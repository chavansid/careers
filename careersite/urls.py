"""careersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls import  url, re_path
from allauth.account.views import confirm_email

urlpatterns = [
    path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^accounts/', include('allauth.urls')),
]