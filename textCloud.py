# -*- coding = utf-8 -*-
# @Time :  20:33
# @Author : 张嘉焜
# @File : textCloud.py
# @software : PyCharm

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图,数据可视乎
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

# 准备词云所需的文字
conn = sqlite3.connect("豆瓣电影Top250.db")
cur = conn.cursor()
sql = "select introduction from doubanTop250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
conn.commit()
cur.close()
conn.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'D:\python\flask_douban\static\assets\img\tree.jpg')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="simkai.ttf",
    width=500,
    height=600
).generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') # 是否显示坐标轴

# plt.show()  # 显示生成的词云图片
plt.savefig(r'D:\python\flask_douban\static\assets\img\words.jpg')
