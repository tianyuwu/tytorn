#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: index.py
@time: 2016/4/22 15:42
"""

# from models.test import test
import json

from handlers.base import MainBaseHandler
import tornado.web
import tornado.gen


class IndexHandler(MainBaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        article = yield self.Query("select * FROM users limit 2")
        print article
        # self.write('恭喜你成功部署tytorn!')
        self.render('index.html', data=article[0])

    def post(self):
        pass