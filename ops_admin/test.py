#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/21/17 3:01 PM
# @Author  : MiracleYoung
# @File    : test.py
# @Software: PyCharm

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(os.path.join(BASE_DIR, 'templates'))
print(BASE_DIR)