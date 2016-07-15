#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/7/11 17:25
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : uuid.py
# @Software: PyCharm
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Page(Base):
    __tablename__ = 'uuid'

    uuid = Column(String(50))
