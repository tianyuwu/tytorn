#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: log.py
@time: 2016/4/25 18:13
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
import tools

class Logger():
    def __init__(self, logname, withuuid=True):
        print 'Init %s Log System...' % logname
        if not os.path.exists('log'):
            os.mkdir('log')
        # 创建一个self.logger
        if withuuid:
            logname = logname + '_' + str(tools.GenerateRandomString(5, False))
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        # filename = 'log/%s_%s.log' % (logname, utils.GetCurrentTime())
        filename ='log/%s.log'%logname
        # fh = logging.FileHandler(filename)
        #     S	秒
        #     M	分钟
        #     H	小时
        #     D	天
        #     W	周
        # midnight	在午夜
        fh = TimedRotatingFileHandler(filename, "D", 1, 0)
        fh.suffix = "%Y%m%d-%H%M%S.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
        #fh.setFormatter(formatter)
        #logging.basicConfig(level=logging.INFO)
        #fileTimeHandler.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        #'%(asctime)s-%(name)s-%(levelname)s-%(message)s'
        formatter = logging.Formatter('[%(asctime)s]%(message)s')
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        # 给self.logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def __del__(self):
        print 'Shutdown Log System...'
        if logging is not None:
            logging.shutdown()

    def Info(self, message, msgbox=None, withreturn=True):
        self.logger.info(message)
        if msgbox is not None:
            if withreturn:
                _outmsg = message + '\n'
            else:
                _outmsg = message

            msgbox.insert('end', _outmsg)



# 全局定义
Log = Logger('App')