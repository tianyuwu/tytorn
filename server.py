#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: server.py
@time: 2016/4/22 15:49
"""
import signal
import time
import sys
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from app import Application
from utils.log import Log

define("port", default=9999, help="run on the given port", type=int)
define("debug", default=True, help="debug or not", type=bool)   # 默认为debug模式,生产环境设为False


# PORT = '9999'
class App:
    def __init__(self):
        self.http_server = None
        self.mainApp = None
        self.io_loop = tornado.ioloop.IOLoop.instance()
        self.deadline = None

    def __del__(self):
        pass


    def sig_handler(self, sig, frame):
        Log.Info('Caught signal: %s'%sig)
        tornado.ioloop.IOLoop.instance().add_callback(self.shutdown)

    def shutdown(self):
        Log.Info('Stopping http server')

        self.http_server.stop()  # 不接收新的 HTTP 请求

        Log.Info('Will shutdown in %s seconds ...'%1)
        # self.io_loop = tornado.ioloop.IOLoop.instance()

        self.deadline = time.time() + 1
        self.stop_loop()

    def stop_loop(self):
        now = time.time()
        if now < self.deadline and (self.io_loop._callbacks or self.io_loop._timeouts):
            self.io_loop.add_timeout(now + 1, self.stop_loop)
        else:
            print 'Server Shutdown!'
            self.io_loop.stop()  # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环

    def Init(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        signal.signal(signal.SIGTERM, self.sig_handler)
        signal.signal(signal.SIGQUIT, self.sig_handler)
        signal.signal(signal.SIGINT, self.sig_handler)
        signal.signal(signal.SIGTSTP, self.sig_handler)
        return True

    def MainLoop(self):
        tornado.options.parse_command_line()
        # if options.debug == 'debug':
        #     import pdb
        #     pdb.set_trace()  #引入相关的pdb模块进行断点调试
        Log.Info('Init Server...')
        self.mainApp = Application(self.io_loop)
        self.http_server = tornado.httpserver.HTTPServer(self.mainApp, xheaders=True)
        self.http_server.listen(options.port)

        # 初始化异步数据库接口
        Log.Info('Server Running in port %s...'% options.port)
        self.io_loop.start()



if __name__ == "__main__":
    app = App()
    if app.Init():
        app.MainLoop()