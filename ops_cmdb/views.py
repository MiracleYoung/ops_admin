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
            'hostname': request.POST.get('server-hostname', ''),
            'ip': request.POST.get('server-ip', ''),
            'type': int(request.POST.get('server-type', 0)),
            'description': request.POST.get('server-description', ''),
            'cmdb_idc_id': int(request.POST.get('server-cmdb-idc-id', 0)),
            'cmdb_cabinet_id': int(request.POST.get('server-cmdb-cabinet-id', 0)),
            'cabinet_unit': int(request.POST.get('server-cabinet-unit', 0)),
            'switch1_id': int(request.POST.get('server-switch1-id', 0)),
            'switch1_port': int(request.POST.get('server-switch1-port', 0)),
            'switch2_id': int(request.POST.get('server-switch2-id', 0)),
            'switch2_port': int(request.POST.get('server-switch2-port', 0)),
            'mgr_id': int(request.POST.get('server-mgr-id', 0)),
            'mgr_port': int(request.POST.get('server-mgr-port', 0)),
        }
        response_data = {}
        try:
            cmdb_server = CmdbServer(**server_form)
            cmdb_server.save()
            response_data['message'] = 'server created success.'
            response_data['ip'] = cmdb_server.ip
            return HttpResponse(json.dumps(response_data))
        except DatabaseError as e:
            response_data['message'] = 'server created failed by {}'.format(e)
            raise HttpResponseBadRequest(json.dumps(response_data))


def get_idc(request):
    if request.method == 'GET':
        idc = CmdbIdc.objects.all().values('name')
        response_data = [item['name'] for item in idc]
        return HttpResponse(json.dumps(response_data))
