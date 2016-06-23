#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: config.py
@time: 2016/4/23 16:56
"""

# postgre配置
DB_HOST = '127.0.0.1'
DB_PORT = 5432
DB_DATABASE = 'sxsdb'
DB_USER = 'dbuser'
DB_PASSWORD = '123kkk'
DB_ASYNC_MAXCONN = 33  # 最大异步连接数
DB_SYNC_MAXCONN = 10  # 最大同步连接数


# redis配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASS = '123kkk'


# session配置
SESSION_SECRET = '3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc'
COOKIE_SECRET = '3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc'
SEESSION_TIMEOUT = 60