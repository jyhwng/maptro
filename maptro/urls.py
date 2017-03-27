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
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from map import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^map/', include('map.urls', namespace="station")),
    url('', include('social_django.urls', namespace='social')),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, { 'template_name': 'logout.html'}),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # http://python-social-auth.readthedocs.io/en/latest/configuration/django.html
    url(r'^mypage/$', views.mypage, name='mypage'),
]
