#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/20 19:22
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : insertionSort.py
# @Software: PyCharm

"""
插入排序
将一个记录插入到已排序好的有序表中，从而得到一个新，记录数增1的有序表。
即：先将序列的第1个记录看成是一个有序的子序列，然后从第2个记录逐个进行插入，直至整个序列有序为止。
要点：设立哨兵，作为临时存储和判断数组边界之用。

时间复杂度也为O(n^2), 比冒泡法和选择排序的性能要更好一些
"""
import random

array = random.sample(range(20), 10)
array = [49, 38, 65, 97, 76, 13, 27, 49]
print(array)
size = len(array)
for i in xrange(size):
    print("第" + str(i + 1) + "趟")
    for j in xrange(i):
        if array[i] < array[j]:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
    print(array)
print(array)
