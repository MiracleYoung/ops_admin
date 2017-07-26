#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:16 PM
# @Author  : MiracleYoung
# @File    : views.py
# @Software: PyCharm


from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import Http404, HttpResponseBadRequest, HttpResponseForbidden

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='ops_account:login')
def index(request):
    return render(request, 'ops_cmdb/ops_index.html', {'text': 'ops_cmdb_index'})



