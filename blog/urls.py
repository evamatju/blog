#coding=utf-8
"""blog URL Configuration

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
from article import views
from django.conf.urls import url, include
#from django.contrib.auth.views import login
from django.contrib import admin
from django.conf.urls import *
from django.conf import settings
from django.views import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^view/(?P<text>[\w\d]+)/(?P<order>[\w\d]+)$',views.home),
    url(r'^view/$',views.home),
    url(r'^add/$',views.add),

    url(r'^list/$',views.list),
    url(r'^del_user/$', views.del_user),
    url(r'^del_order/$', views.del_order),

    url(r'^login/$', views.admin_login),
    url(r'^logout/$',views.admin_logout),
    url(r'^add_order/$',views.add_order),
    url(r'^list_order/$', views.list_order),
    url(r'^get_order/$', views.get_order),
    url(r'^get_user/$', views.get_user),
    url(r'^ch_pw/$', views.ch_pw),
    url(r'^ch_order/$', views.ch_order),
    url(r'^device_query/$', views.device_query),

    url(r'^a/(?P<path>.*)$',static.serve,{'document_root':settings.STATIC_URL}),


]
