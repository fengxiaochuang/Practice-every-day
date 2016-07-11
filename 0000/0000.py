#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/7/11 16:27
# @Author  : XIAOCHUANG
# @Site    : www.fengxiaochuang.com/ 
# @File    : 0000.py
# @Software: PyCharm

from PIL import Image, ImageDraw, ImageFont
import random

# 读取图像

fontSize = 150
fontTTF = 'YaHei.Consolas.1.11b.ttf'

img = Image.open('D:/Documents/Pictures/7012438bjw8el75mv3615j20k00k0my5.jpg')
hight, width = img.size
drawPostionRight = width - fontSize + 30
font = ImageFont.truetype(fontTTF, fontSize)
draw = ImageDraw.Draw(img)

msgNum = random.randint(1, 10)
draw.text((drawPostionRight, -30), unicode(msgNum), (255, 0, 0), font=font)
img.show()
# img.save("D:/Documents/Pictures/0000.jpg", 'JPEG')

# # 显示图像
# im.show()
