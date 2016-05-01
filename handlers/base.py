#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: base.py
@time: 2016/4/23 11:43
"""
import tornado.web
from utils.postgredb import PostgreDb
from utils.httpresponse import Response
import pyrestful.rest

class MainBaseHandler(tornado.web.RequestHandler, PostgreDb):

    def get_current_user(self):
        pass

    def write_error(self, status_code, **kwargs):
        self.write('404')
        # self.render('404.html', error_code=status_code)

class RestBaseHandler(pyrestful.rest.RestHandler, PostgreDb, Response):
    def get_current_user(self):
        pass