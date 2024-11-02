"""
URL configuration for Myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from FirstApp import views
from MultiViewsApp import views as v1;
from App1 import views as v11;
from App2 import views as v22;
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path('welcome2/',views.show),
    path('hello/',views.radha),
    path('radha/',views.senddatetime),
    path('hyder/',views.krishna),
    path('mrng/',v1.f1),
    path('after/',v1.f2),
    path('evening/',v1.f3),
    path('hey/',v11.f11),
    path('krsn/',v22.f22),
    path('firstdemo/',views.demo),
    path('secondtdemo/',views.demo),
    path('thirddemo/',views.demo),

    ##Single Project  with multiple applications....

]
