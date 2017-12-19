#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sql_test.py
# @Author: Derek
# @Date  : 2017/12/19
# @Desc  : 无法使用本地已安装的包点settings-project interpreter-齿轮按钮-add local -勾上inherit global site-packages

import unittest
import pymssql


class MyTestCase(unittest.TestCase):
    server='1.1.1.1'
    user='sa'
    password='111111'
    database='test_db'
    table_name='tset_table'

    def test_something(self):

        #以下内容来自http://pymssql.org/en/latest/pymssql_examples.html
        # from os import getenv
        # import pymssql
        #
        # server = getenv("PYMSSQL_TEST_SERVER")
        # user = getenv("PYMSSQL_TEST_USERNAME")
        # password = getenv("PYMSSQL_TEST_PASSWORD")
        # conn = pymssql.connect(server, user, password, "tempdb")
        #
        conn = pymssql.connect(server=self.server, user=self.user, password=self.password,database=self.database)
        cursor = conn.cursor()

        # cursor.execute("""
        # IF OBJECT_ID('persons', 'U') IS NOT NULL
        #     DROP TABLE persons
        # CREATE TABLE persons (
        #     id INT NOT NULL,
        #     name VARCHAR(100),
        #     salesrep VARCHAR(100),
        #     PRIMARY KEY(id)
        # )
        # """)
        # cursor.executemany(
        #     "INSERT INTO persons VALUES (%d, %s, %s)",
        #     [(1, 'John Smith', 'John Doe'),
        #      (2, 'Jane Doe', 'Joe Dog'),
        #      (3, 'Mike T.', 'Sarah H.')])
        # # you must call commit() to persist your data if you don't set autocommit to True
        # conn.commit()

        cursor.execute('SELECT * FROM %s WHERE userid < %s'%(self.table_name,'10'))
        row = cursor.fetchone()
        while row:
            print("userID=%d, UserName=%s,Email=%s" % (row[0], row[2],row[4]))
            row = cursor.fetchone()

        conn.close()


if __name__ == '__main__':
    unittest.main()
