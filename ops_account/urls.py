#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 上午10:55
# @Author  : MiracleYoung
# @File    : urls.py

from django.conf.urls import url
from . import views

app_name = 'ops_account'

urlpatterns = [
    url(r'^login/$', views.ops_login, name='login'),
    url(r'^register/$', views.ops_register, name='register'),
    url(r'^reset/$', views.ops_reset, name='reset'),
    url(r'^reset_password/$', views.ops_reset_password, name='reset_password'),
    url(r'^logout/$', views.ops_logout, name='logout'),
]
