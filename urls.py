#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: urls.py
@time: 2016/4/22 15:41
"""

from handlers import main, blog, admin
from handlers.api.user_api import *
from utils import tools

sub_urls = []

# 主域名路由配置
main_urls = [
    (r'/', main.IndexHandler),
]

admin_urls = ["^admin.dev_sites.com$", [
    (r'/', admin.IndexHandler),
]]

blog_urls = ["^blog.dev_sites.com$", [
    (r'/', blog.IndexHandler),
]]

# rest api配置
rest_handlers = [EchoHandler, TestHandler]



restservices = []
for r in rest_handlers:
    svs = tools.GenerateRestServices(r)  # 组装路由与handler的映射
    restservices += svs
main_urls.extend(restservices)

sub_urls.append(admin_urls)
sub_urls.append(blog_urls)