#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/7/11 16:54
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : 0001..py
# @Software: PyCharm
import random
import hashlib

import time


def createUUID():
    """
    生成UUID
    生成算法 随机数md5前8位 + 时间戳 + md5 后8位
    :return:
    """
    randomNum = random.random()
    md5 = hashlib.md5(str(randomNum)).hexdigest()
    return md5[:8] + "-" + str(int(time.time())) + "-" + md5[-8:]


if __name__ == '__main__':
    for i in range(0, 200):
        uuid = createUUID()
        print uuid
