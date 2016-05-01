#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: admin.py
@time: 2016/4/30 16:56
"""
import tornado.gen
import datetime
from pyrestful import mediatypes
from pyrestful.rest import get
from handlers.base import RestBaseHandler
from utils.httpresponse import ResponseCode as Code

class EchoHandler(RestBaseHandler):
     @get(_path="/echo/{name}", _produces=mediatypes.APPLICATION_JSON)
     def hello(self, name):
          data = {"Hello": name}
          return self.make_response(Code.SUCCESS, content=data)


class TestHandler(RestBaseHandler):
     @get(_path="/test", _produces=mediatypes.APPLICATION_JSON, _async=True)
     @tornado.gen.coroutine
     def hello(self, obj):
          article = yield obj.QueryNoParam("select * FROM articles")
          raise tornado.gen.Return(self.make_response(Code.SUCCESS, content=article))

