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
from django.db import DatabaseError

from .models import CmdbServer, CmdbIdc, CmdbCabinet, CmdbSwitch
import json


@login_required
def index(request):
    return render(request, 'ops_cmdb/cmdb_index.html', {'h1': 'CMDB', 'h2': '', 'text': 'ops_cmdb_index'})


@login_required
def create_server(request):
    if request.method == 'GET':
        return render(request, 'ops_cmdb/cmdb_create_server.html')
    if request.method == 'POST':
        server_form = {
            'hostname': request.POST.get('hostname', ''),
            'ip': request.POST.get('ip', ''),
            'project': request.POST.get('project', ''),
            'description': request.POST.get('description', ''),
            'cmdb_idc_id': request.POST.get('cmdb_idc_id', ''),
            'cmdb_cabinet_id': request.POST.get('cmdb_cabinet_id', ''),
            'cabinet_unit': request.POST.get('cabinet_unit', ''),
            'switch1_id': request.POST.get('switch1_id', ''),
            'switch1_port': request.POST.get('switch1_port', ''),
            'switch2_id': request.POST.get('switch2_id', ''),
            'switch2_port': request.POST.get('switch2_port', ''),
            'mgr_id': request.POST.get('mgr_id', ''),
            'mgr_port': request.POST.get('mgr_port', ''),
        }
        response_data = {}
        try:
            cmdb_server = CmdbServer(server_form)
            cmdb_server.save()
            response_data['message'] = 'server created success.'
            return HttpResponse(json.dumps(response_data))
        except DatabaseError as e:
            response_data['message'] = 'server created failed by {}'.format(e)
            raise HttpResponseBadRequest(json.dumps(response_data))


def get_idc(request):
    if request.method == 'GET':
        idc = CmdbIdc().objects.all().only('name')
        return HttpResponse(json.dumps({'idc': idc}))
