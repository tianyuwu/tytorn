#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: application.py
@time: 2016/4/22 15:48
"""

import tornado.web
import os

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
    cookie_secret="set cookie secret",
    login_url="/auth/login",
    debug=True,
    allow_remote_access=True,
    # static_url_prefix="",  # static路径的前缀配置，在生产环境可以配置cdn
    # ui_modules=UIModules,
    # ui_methods=UIMethods
)


class Application(tornado.web.Application):
    def __init__(self):
        from urls import main_urls, sub_urls
        settings = SETTINGS

        super(Application, self).__init__(handlers=main_urls, **settings)

        for sub_url in sub_urls:
            self.add_handlers(sub_url[0], sub_url[1])
