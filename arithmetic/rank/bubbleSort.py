#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/20 18:52
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : bubble_sort.py
# @Software: PyCharm
"""
冒泡排序
基本思想是:两两比较相邻记录的关键字,如果反序则交换
冒泡排序时间复杂度最好的情况为O(n),最坏的情况是O(n^2)
"""
import random

array = random.sample(range(20), 10)
array = [0, 4, 5, 3, 13, 12, 10, 17, 18, 19]
print(array)
size = len(array)
for i in xrange(size - 1):
    print("第" + str(i + 1) + "趟")
    print(array)
    isChange = False  # 增加状态位判断是否发生改变
    if i == 0 or isChange:
        for j in xrange(size - 1):
            if array[j] > array[j + 1]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
                isChange = True
            else:
                pass
    else:
        break
print("最终结果")
print(array)
