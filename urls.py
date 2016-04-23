#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: urls.py
@time: 2016/4/22 15:41
"""

from handlers import main, blog, admin

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

sub_urls.append(admin_urls)
sub_urls.append(blog_urls)