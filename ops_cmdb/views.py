#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:16 PM
# @Author  : MiracleYoung
# @File    : views.py
# @Software: PyCharm


from django.shortcuts import render


def index(request):
    return render(request, 'ops_cmdb/index.html', {'text': 'ops_cmdb_index'})
