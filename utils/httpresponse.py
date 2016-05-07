#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#
#   Author  :   YunJianFei
#   E-mail  :   yunjianfei@126.com
#   Date    :   2014/02/25
#   Desc    :   Test db
#
#
import logging
import tools

class ResponseCode:
    SUCCESS = 0
    NO_PARAMETER = 1
    INVALID_PARAMETER = 2
    HAS_EXISTED = 3
    DB_ERROR = 4
    NO_RECORD = 5

    code_string_EN = {
        SUCCESS : "SUCCESS",
        NO_PARAMETER : "NO_PARAMETER",
        INVALID_PARAMETER : "INVALID_PARAMETER",
        HAS_EXISTED : "HAS_EXISTED",
        DB_ERROR : "DB_ERROR",
        NO_RECORD : "NO_RECORD",
    }

    failure_reason_EN = {
        SUCCESS : "",
        NO_PARAMETER : "There is no parameter '%s'!",
        INVALID_PARAMETER : "The value of parameter '%s' is invalid!",
        HAS_EXISTED : "This object has existed in the table '%s'!",
        DB_ERROR : "Database error when execute '%s'!",
        NO_RECORD : "No record when query '%s'!",
    }

class Response:
    def to_int(self, num):
        if num is None:
            return num

        try:
            num = tools.strip_string(num) 
            value = int(num)
            return value
        except Exception, ex:
            logging.error("Convert '%s' to Int Error: %s", str(num), str(ex))
            return None


    def make_response(self, code, para=None, content=None, err_str=None):
        response = {'code': code, 'code_msg': ResponseCode.code_string_EN[code]}

        failure_reason = ""
        if code != ResponseCode.SUCCESS:
            if para is not None:
                failure_reason = ResponseCode.failure_reason_EN[code] % para

            if err_str is not None:
                failure_reason = failure_reason + err_str

            response['failure_reason'] = failure_reason

        if content is not None:
            response['data'] = content

        return response
