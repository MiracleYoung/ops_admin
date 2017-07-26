#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 上午11:00
# @Author  : MiracleYoung
# @File    : ops_account.py


from lib.utils import Mail

if __name__ == '__main__':


    message = '''Hi, {}, your new password is '{}'. '''.format('miracle', '111111')
    subject = 'Ops Admin Reset Password Email'
    recipient_list = ['me@miracle.com', ]
    try:
        Mail.send_mail(subject=subject, message=message, recipient_list=recipient_list)
    except Exception as e:
        print(e)
