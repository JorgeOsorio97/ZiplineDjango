"""ZiplineDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from ShowIndicators import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'ShowIndicators'

urlpatterns = [
    re_path(r'^pruebaPOST/$',views.pruebasPost, name='pruebaPost'),
    re_path(r'^get-data/$', views.getData, name='get-data'),
    re_path(r'^result/$', views.result, name='result'),
    re_path(r'^bestStrategy/$', views.callBestStrategy, name = 'bestStrategy'),
    re_path(r'^add_security/$', views.addSecurity, name = 'addSecurity'),
    re_path(r'^new_security/$', views.newSecurity, name = 'newSecurity'),
    re_path(r'strategy_creator/$', views.strategyCreator, name = 'strategyCreator'),
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()