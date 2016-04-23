#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: index.py
@time: 2016/4/22 15:42
"""

from models.test import test
from handlers.base import MainBaseHandler

class IndexHandler(MainBaseHandler):
    def get(self):
        test_model = test()
        self.write(test_model.f())