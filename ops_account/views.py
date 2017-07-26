#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 上午10:55
# @Author  : MiracleYoung
# @File    : views.py


from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http import Http404, HttpResponseBadRequest

from lib.utils import Mail

import json


def ops_login(request):
    '''
    GET: login page
    POST: login api
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'ops_account/ops_login.html')
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(email=email).first()
        if user is not None and user.check_password(password) and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('ops_cmdb:index'))
        else:
            return render(request, 'ops_account/ops_login.html',
                          {'error_message': 'user is not exist or password is wrong.'})


def ops_register(request):
    '''
    GET: register page
    POST: register api
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'ops_account/ops_register.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        repassword = request.POST.get('repassword', '')
        is_staff = 1
        is_active = 1
        if password == repassword:
            if not User.objects.filter(email=email).first():
                if not User.objects.filter(username=username).first():
                    user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password=password,
                                                    is_staff=is_staff,
                                                    is_active=is_active)
                    user.save()
                    return HttpResponseRedirect(reverse('ops_cmdb:index'))
                else:
                    return render(request, 'ops_account/ops_register.html', {'error_message': 'username is registered'})
            else:
                return render(request, 'ops_account/ops_register.html', {'error_message': 'email is registered'})
        else:
            return render(request, 'ops_account/ops_register.html', {'error_message': 'password is not same'})


def ops_reset(request):
    '''
    reset password page
    :param request:
    :return:
    '''
    return render(request, 'ops_account/ops_reset.html')


def ops_reset_password(request):
    '''
    reset password api
    :param request:
    :return:
    '''
    response_data = {}
    if request.method == 'GET':
        email = request.GET.get('email', '')
        user = User.objects.filter(email=email).first()
        if user is not None:
            new_password = '111111'
            message = '''Hi, {}, your new password is '{}'. '''.format(user.username, new_password)
            subject = 'Ops Admin Reset Password Email'
            recipient_list = [user.email, ]
            user.set_password(new_password)
            try:
                Mail.send_mail(subject=subject, message=message, recipient_list=recipient_list)
                response_data['message'] = 'reset password email is sent.'
                return HttpResponse(json.dumps(response_data), content_type='application/json')
            except Exception as e:
                response_data['message'] = 'email got something wrong >> {}'.format(e)
                raise HttpResponseBadRequest(json.dumps(response_data), content_type='application/json')
        response_data['message'] = 'email is not exist'
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        response_data['message'] = 'request is wrong.'
        raise HttpResponseBadRequest(json.dumps(response_data), content_type='application/json')


def ops_logout(request):
    '''
    logout
    :param request:
    :return:
    '''
    logout(request)
    return HttpResponseRedirect(reverse('ops_account:login'))