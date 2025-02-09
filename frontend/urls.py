"""
URL configuration for frontend project.

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
from django.urls import path, re_path
from app.views import login, logout, register, profile, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.IndexView.as_view(), name='index'),
    re_path(r'^(?P<page>.+\.html)$', index.IndexView.as_view(), name='index'),
    re_path(r'^(?P<page>.+\.css)$', index.IndexView.as_view(), name='index'),
    path('profile/', profile.ProfileView.as_view(), name='profile'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('logout/', logout.LogoutView.as_view(), name='logout'),
]
