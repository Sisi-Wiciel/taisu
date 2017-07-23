# -*- coding: utf-8 -*-
import jieba
import re
import csv
import wordcloud
import matplotlib.pyplot as plt
# import os
# pwd = os.getcwd()
# print(pwd)
file_ad = r"439-黄帝内经太素[204].txt"
str = open(file_ad,encoding='gb2312')
with str as f:
    data = f.read()

pattern=re.compile('(?<=\[)[^\[.]+?(?=\])')
search = pattern.findall(data)
# print(search)
if search:
    for group in search:
        seg_list = jieba.cut(group,cut_all=False)
        print(",".join(seg_list))

# wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
wordcloud = WordCloud(font_path=u'./static/simheittf/simhei.ttf',
                      background_color="black", margin=5, width=1800, height=800)

wordcloud = wordcloud.generate(seg_list)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
