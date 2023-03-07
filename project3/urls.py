"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from appno1.views import *
from appno2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appno1/', appno1,name='appno1'),
    path('appno1second/',appno1second,name='appno1second'),
    path('appno2/',appno2,name='appno2'),
    path('appno2second/',appno2second,name='appno2second')
]
