#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:16 PM
# @Author  : MiracleYoung
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from . import views

app_name = 'ops_cmdb'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_server/$', views.create_server, name='create_server'),
    url(r'^get_idc/$', views.get_idc, name='get_idc'),
]
