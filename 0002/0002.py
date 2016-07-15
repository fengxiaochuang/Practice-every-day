#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/7/11 17:17
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : 0002.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import createUUID

# 初始化数据库连接:
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/test?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
db = DBSession()
for i in range(0, 200):
    sql = 'insert into uuid (uuid) values (:guid)'
    uuid = createUUID.createUUID()
    data = db.execute(sql, {'guid': uuid})
    print data
print "all complete"
