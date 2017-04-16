#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/20 19:49
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : simpleSort.py
# @Software: PyCharm
"""
通过n-i次关键字之间的比较,从n-i+1 个记录中选择关键字最小的记录,并和第i(1<=i<=n)个记录交换之
尽管与冒泡排序同为O(n^2),但简单选择排序的性能要略优于冒泡排序
"""
import random

array = random.sample(range(20), 10)
array = [49, 38, 65, 97, 76, 13, 27, 49]
size = len(array)
for i in xrange(size):
    min = array[0]
    for j in xrange(size - i):
        if min > array[j]:
            min = array[i]
    
