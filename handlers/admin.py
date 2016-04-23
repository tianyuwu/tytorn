#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: admin.py
@time: 2016/4/22 16:56
"""
import tornado.web
from models.test import test

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        test_model = test()
        self.write(test_model.f() + '_admin')