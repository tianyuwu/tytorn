#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: index.py
@time: 2016/4/22 15:42
"""

# from models.test import test
from handlers.base import MainBaseHandler
import tornado.web
import tornado.gen


class IndexHandler(MainBaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # article = yield self.QueryNoParam("select * FROM articles")
        # print article[0]['title']
        self.write('恭喜你成功部署tytorn!')