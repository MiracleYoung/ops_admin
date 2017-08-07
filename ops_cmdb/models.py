#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:17 PM
# @Author  : MiracleYoung
# @File    : models.py
# @Software: PyCharm



from django.db.models import Model, IntegerField, CharField, DateTimeField, SmallIntegerField
from django.utils import timezone


class CmdbServer(Model):
    id = IntegerField(primary_key=True, auto_created=True)
    hostname = CharField(max_length=255, null=False, default='')
    ip = CharField(max_length=32, null=False, default='')
    project = CharField(max_length=255, null=False, default='')
    description = CharField(max_length=512, null=False, default='')
    cmdb_idc_id = IntegerField(null=False, default=0)
    cmdb_cabinet_id = IntegerField(null=False, default=0)
    cabinet_unit = IntegerField(null=False, default='0')
    switch1_id = IntegerField(null=False, default=0)
    switch1_port = IntegerField(null=False, default=0)
    switch2_id = IntegerField(null=False, default=0)
    switch2_port = IntegerField(null=False, default=0)
    mgr_id = IntegerField(null=False, default=0)
    mgr_port = IntegerField(null=False, default=0)
    create_time = DateTimeField(null=False, default=timezone.now)
    update_time = DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'cmdb_server'


class CmdbIdc(Model):
    id = IntegerField(primary_key=True, auto_created=True)
    name = CharField(max_length=255, null=False, default='')
    create_time = DateTimeField(null=False, default=timezone.now)
    update_time = DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'cmdb_idc'


class CmdbCabinet(Model):
    id = IntegerField(primary_key=True, auto_created=True)
    name = CharField(max_length=255, null=False, default='')
    cmdb_idc_id = IntegerField(null=False, default=0)
    create_time = DateTimeField(null=False, default=timezone.now)
    update_time = DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'cmdb_cabinet'


class CmdbSwitch(Model):
    id = IntegerField(primary_key=True, auto_created=True)
    name = CharField(max_length=255, null=False, default='')
    cmdb_cabinet_id = IntegerField(null=False, default=0)
    create_time = DateTimeField(null=False, default=timezone.now)
    update_time = DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'cmdb_switch'
