#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/7 13:52
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : 0001.py
# @Software: PyCharm
dataset = (
    (1, -890),
    (2, -1411),
    (2, -1560),
    (3, -2220),
    (3, -2091),
    (4, -2878),
    (5, -3537),
    (6, -3268),
    (6, -3920),
    (6, -4163),
    (8, -5471),
    (10, -5157),
)

args = (
    (-1780.0, 530.9),
    (-1780.0, -530.9),
    (-569.6, 530.9),
    (-569.6, -530.9)
)

for a, b in args:
    print a, b
    for x, y in dataset:
        print (a + b * x), y
    print("==========================")
