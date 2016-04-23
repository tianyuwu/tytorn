#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: base.py
@time: 2016/4/23 11:43
"""
import tornado.web

class MainBaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get_current_user(self):
        pass

    def write_error(self, status_code, **kwargs):
        self.render('404.html', error_code=status_code)