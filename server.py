#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: server.py
@time: 2016/4/22 15:49
"""
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from application import Application


define("port", default=9999, help="run on the given port", type=int)


# PORT = '9999'

def main():
    tornado.options.parse_command_line()
    print("Starting tornado web server on http://127.0.0.1:%s" % options.port)
    print("Quit the server with CONTROL-C")
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()