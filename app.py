#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: app.py
@time: 2016/4/22 15:48
"""

import tornado.web
import os
from tornado.options import options
from config import *
from utils import postgredb

import momoko
from psycopg2.extras import RealDictCursor
from utils import session
from utils.log import Log


class Application(tornado.web.Application):

    def __init__(self, ioloop):
        from urls import main_urls, sub_urls
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=3600,
            store_options={
                'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': 'baidapang',
            },
            login_url="/auth/login",
            debug=options.debug,
            allow_remote_access=True,
            # static_url_prefix="",  # static路径的前缀配置，在生产环境可以配置cdn
            # ui_modules=UIModules,
            # ui_methods=UIMethods


        )

        dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
        DB_DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

        # pg 异步连接池
        postgredb.mk_pool = momoko.Pool(
            dsn=dsn,
            size=1,
            max_size=DB_ASYNC_MAXCONN,
            ioloop=ioloop,
            setsession=("SET TIME ZONE PRC",),
            raise_connect_errors=False,
            cursor_factory=RealDictCursor,  # 设置返回结果集为字典形式,不设置的话只是一个tupple
        )

        # this is a one way to run ioloop in sync
        future = postgredb.mk_pool.connect()
        ioloop.add_future(future, lambda f: ioloop.stop())
        ioloop.start()

        future = postgredb.mk_pool.register_json()
        # This is the other way to run ioloop in sync
        ioloop.run_sync(lambda: future)
        Log.Info('Current Postgresql Version:%s'%postgredb.mk_pool.server_version)
        super(Application, self).__init__(handlers=main_urls, **settings)

        for sub_url in sub_urls:
            self.add_handlers(sub_url[0], sub_url[1])

        self.session_manager = session.SessionManager(settings["session_secret"], settings["store_options"], settings["session_timeout"])
