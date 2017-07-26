#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 下午5:08
# @Author  : MiracleYoung
# @File    : utils.py

from django.core import mail


class Mail:
    @classmethod
    def send_mail(cls, subject='', message='', from_email='yangqinglin_0723@163.com', recipient_list=None,
                  html_message=None):
        mail.send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
                       html_message=html_message)
