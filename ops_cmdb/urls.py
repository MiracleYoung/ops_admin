#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:16 PM
# @Author  : MiracleYoung
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from . import views

app_name = 'cmdb'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
