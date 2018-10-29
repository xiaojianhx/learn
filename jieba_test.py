#!/usr/bin/python3
# encoding: utf-8

import jieba

jieba.load_userdict("userdict.txt")
jieba.add_word('一妻一妾一人生', None, 'nl')
# jieba.enable_parallel(4)

s = '一天一地一世界，一妻一妾一人生'
seg_list = jieba.cut(s, HMM = False)
print("HMM Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(s, cut_all = True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(s, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(s)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(s)  # 搜索引擎模式
print(", ".join(seg_list))


print ('############################################### %s ###############################################' % 'tags')
import jieba.analyse

tags = jieba.analyse.extract_tags(s, withWeight = True, topK = 10)

for tag in tags:
    print (tag)

print ('############################################### %s ###############################################' % '词性')
import jieba.posseg
words = jieba.posseg.cut(s)
for word in words:
    print (word)

print ('############################################### %s ###############################################' % '出现位置')
result = jieba.tokenize(s)
for item in result:
    print (item)


print ('############################################### %s ###############################################' % '搜索模式')
result = jieba.tokenize(s, mode = 'search')
for item in result:
    print (item)