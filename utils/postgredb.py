#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0.0
@author: whitney
@file: pgdb.py
@time: 2016/4/23 17:34
"""
import tornado.gen
import datetime
import tools

mk_pool = None  # momoke连接池实例

class PostgreDb(object):
    """
    postgre的异步数据库操作类
    """
    def __init__(self):
        self.adb_trans = []
        super(PostgreDb, self).__init__()


    @tornado.gen.coroutine
    def Exec(self, sqlstr, *parm):
        """
        执行插入或者更新，返回true或者false
        :param sqlstr:
        :param parm:
        :return:
        """
        tools.PrintSqlStr(sqlstr, parm)
        rv = True
        try:
            cursor = yield mk_pool.execute(sqlstr, parm)
            if not cursor:
                rv = False

        except Exception as e:
            #self.PrintSqlStr(sqlstr, parm)
            errormsg = '[sqlerrror]' + repr(e)
            print errormsg
            rv = False

        finally:
            raise tornado.gen.Return(rv)

    def TransExec(self, sqlstr, *parm):
        """
        进行事务
        :param sqlstr:
        :param parm:
        :return:
        """
        tools.PrintSqlStr(sqlstr, parm)
        if not self.adb_trans:
            self.adb_trans = []

        sqltask = [sqlstr, parm]
        self.adb_trans.append(sqltask)

    @tornado.gen.coroutine
    def TransCommit(self):
        """
        提交事务
        :return:
        """
        rv = True
        try:
            cursors = yield mk_pool.transaction(self.adb_trans)
            if not cursors:
                rv = False

        except Exception as e:
            errormsg = '[sqlerrror]' + repr(e)
            print errormsg
            rv = False

        finally:
            self.adb_trans = []
            raise tornado.gen.Return(rv)

    @tornado.gen.coroutine
    def Query(self, sqlstr, *parm):
        """
        执行查询，返回多条结果
        :param sqlstr:
        :param parm:
        :return:
        """
        rv = []
        tools.PrintSqlStr(sqlstr, parm)

        try:
            cursor = yield mk_pool.execute(sqlstr, parm)
            _fetch = cursor.fetchall()
            if _fetch:
                rv = _fetch
                if rv:
                    # 结果中如果有datetime类型，转换为对应的字符串
                    for row in rv:
                        for k, v in row.items():
                            if isinstance(v, datetime.datetime):
                                row[k] = v.strftime('%Y-%m-%d %H:%M:%S')

        except Exception as e:
            errormsg = '[sqlerrror]' + repr(e)
            print errormsg
            raise errormsg

        finally:
            raise tornado.gen.Return(rv)

    @tornado.gen.coroutine
    def QueryOne(self, sqlstr, *parm):
        """
        执行查询，返回一条结果
        :param sqlstr:
        :param parm:
        :return:
        """
        rv = []
        tools.PrintSqlStr(sqlstr, parm)

        try:
            cursor = yield mk_pool.execute(sqlstr, parm)
            _fetch = cursor.fetchall()
            if _fetch:
                rv = _fetch

                if rv:
                    # 结果中如果有datetime类型，转换为对应的字符串
                    for row in rv:
                        for k, v in row.items():
                            if isinstance(v, datetime.datetime):
                                row[k] = v.strftime('%Y-%m-%d %H:%M:%S')

        except Exception as e:
            errormsg = '[sqlerrror]' + repr(e)
            print errormsg
            raise errormsg

        finally:
            raise tornado.gen.Return(rv[0])