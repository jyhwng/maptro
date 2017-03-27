"""maptro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from map import views

urlpatterns = [
    url(r'^(?P<station_pk>\d+)/$', views.station_detail, name="station_detail"),
    url(r'^(?P<station_pk>\d+)/(?P<nick_pk>\d+)/like/$', views.nick_like, name="nick_like"),
    url(r'^(?P<station_pk>\d+)/(?P<nick_pk>\d+)/delete/$', views.nick_delete, name="nick_delete"),  # /delete/ 안해줬을때, redirect 는 잘 되어서 http 302 나오지만 실제로 살제는 안됨. 다른 url과 패턴이 똑같았기 때문
]
