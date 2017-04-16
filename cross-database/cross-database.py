#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 21:23
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : cross-database.py
# @Software: PyCharm

import MySQLdb

"""
Mysql 跨库连接
"""
conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    charset="UTF8"
)
# 获取游标
cur = conn.cursor()

# 收影响条数
rows_length = cur.execute("select * from kppw.kppw_users as kk join test.user as tu on tu.user_id = kk.id")
print(rows_length)
# 拿到数据
rows_data = cur.fetchall()
print(rows_data)
# 后续处理
cur.close()
# 隐隐约约记得默认是auto_commit = false, 需要手动commit
conn.commit()
conn.close()
