"""vb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from cover import views as cover_views
from profiles import views as profiles_views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="index"),
    url(r'^$', cover_views.get_index),
    url(r'^register/$', profiles_views.register, name='register'),
    url(r'^login/$', profiles_views.login, name='login'),
    url(r'^logout/$', profiles_views.logout, name='logout'),
    url(r'^profile/$', profiles_views.profile, name='profile'),
]
