#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: tools.py
@time: 2016/4/23 17:42
"""
import random
import re
import string
import logging
from datetime import date, datetime

def strip_string(ori):
    # if isinstance(ori, str):
    if ori is None:
        return ori

    ori = str(ori)
    ori = ori.strip("\'")
    ori = ori.strip("\"")
    return ori

def to_int(num):
    if num is None:
        return num

    try:
        num = strip_string(num)
        value = int(num)
        return value
    except Exception, ex:
        logging.error("Convert '%s' to Int Error: %s", str(num), str(ex))
        return None

def to_encode(ustr, encoding='utf-8'):
    if ustr is None:
        return ''
    if isinstance(ustr, unicode):
        return ustr.encode(encoding, 'ignore')
    else:
        return str(ustr)

def json_date_default(obj):
    if isinstance(obj, datetime):
        # return obj.strftime('%Y-%m-%d %H:%M:%S')
        return str(obj)
    elif isinstance(obj, date):
        # return obj.strftime('%Y-%m-%d')
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)

def PrintSqlStr(sqlstr, parm):
    """
    打印sql语句
    :param sqlstr:
    :param parm:
    :return:
    """
    _parm = []
    for p in parm:
        _parm.append("'%s'" % p)
    outstr = sqlstr % tuple(_parm)
    print outstr.decode('utf-8')


#withpunctuation是否带标点符号
def GenerateRandomString(length, withpunctuation = True, withdigit = True):
    """
    Linux正则命名参考：http://vbird.dic.ksu.edu.tw/linux_basic/0330regularex.php#lang
    [:alnum:]	代表英文大小写字节及数字，亦即 0-9, A-Z, a-z
    [:alpha:]	代表任何英文大小写字节，亦即 A-Z, a-z
    [:blank:]	代表空白键与 [Tab] 按键两者
    [:cntrl:]	代表键盘上面的控制按键，亦即包括 CR, LF, Tab, Del.. 等等
    [:digit:]	代表数字而已，亦即 0-9
    [:graph:]	除了空白字节 (空白键与 [Tab] 按键) 外的其他所有按键
    [:lower:]	代表小写字节，亦即 a-z
    [:print:]	代表任何可以被列印出来的字节
    [:punct:]	代表标点符号 (punctuation symbol)，亦即：" ' ? ! ; : # $...
    [:upper:]	代表大写字节，亦即 A-Z
    [:space:]	任何会产生空白的字节，包括空白键, [Tab], CR 等等
    [:xdigit:]	代表 16 进位的数字类型，因此包括： 0-9, A-F, a-f 的数字与字节

    Python自带常量(本例中改用这个，不用手工定义了)
    string.digits		  #十进制数字：0123456789
    string.octdigits	   #八进制数字：01234567
    string.hexdigits	   #十六进制数字：0123456789abcdefABCDEF
    string.ascii_lowercase #小写字母(ASCII)：abcdefghijklmnopqrstuvwxyz
    string.ascii_uppercase #大写字母(ASCII)：ABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.ascii_letters   #字母：(ASCII)abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.punctuation	 #标点符号：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    以下的不用，有locale问题
    string.lowercase	   #abcdefghijklmnopqrstuvwxyz
    string.uppercase	   #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.letters		 #ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

    以下的不能用
    string.whitespace	  #On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
    string.printable	   #digits, letters, punctuation, and whitespace
    """
    punctuation = '!$%^&*'

    rdw_seed = string.ascii_letters

    if withdigit:
        rdw_seed += string.digits

    if withpunctuation:
        rdw_seed += punctuation

    rdw = []
    while len(rdw) < length:
        rdw.append(random.choice(rdw_seed))
    return ''.join(rdw)


def GenerateRestServices(rest):
    svs = []
    paths = rest.get_paths()
    for p in paths:
        s = re.sub(r"(?<={)\w+}", ".*", p).replace("{", "")
        o = re.sub(r"(?<=<)\w+", "", s).replace("<", "").replace(">", "").replace("&", "").replace("?", "")
        svs.append((o, rest))
    return svs