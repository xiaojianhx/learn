#!/usr/bin/python3
# encoding: utf-8

import jieba
import jieba.analyse

text = '真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系'

str1 = jieba.cut(text, cut_all=True)
print ('全模式分词：', '|'.join(str1))

str2 = jieba.cut(text, cut_all=True, HMM=False)
print ('全模式分词：', '|'.join(str2))

str3 = jieba.cut(text, cut_all=False)
print ('全模式分词：', '|'.join(str3))

str4 = jieba.cut(text, cut_all=False, HMM=False)
print ('全模式分词：', '|'.join(str4))

str5 = jieba.cut_for_search(text)
print ('搜索引擎模式分词：', '|'.join(str5))

str6 = jieba.analyse.extract_tags(text)
print ('关键词：', '|'.join(str6))

str7 = jieba.analyse.extract_tags(text, topK=3)
print ('关键词：', '|'.join(str7))