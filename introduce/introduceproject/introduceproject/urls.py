"""introduceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from introduceapp.views import home, hobby, music, picture, place, rollingpaper



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('hobby/', hobby, name="hobby"),
    path('music/', music, name="music"),
    path('picture/', picture, name="picture"),
    path('place/', place, name="place"),
    path('rollingpaper/', rollingpaper, name="rollingpaper"),
    path('rollingpaper/', include('introduceapp.urls')),
]
