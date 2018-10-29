#!/usr/bin/python3
# encoding: utf-8

print ('############################################### %s ###############################################' % '基本信息')
from nltk.corpus import brown
print (brown.categories())
print (brown.fileids())
# print (len(brown.sents()))
# print (len(brown.words()))

print ('############################################### %s ###############################################' % '分析')
import nltk
s0 = 'hello, world'
s1 = '一天一地一世界，一妻一妾一人生'

tokens = nltk.word_tokenize(s0)
print (tokens)


tokens = nltk.word_tokenize(s1)
print (tokens)

print ('############################################### %s ###############################################' % '中文分词')
import jieba
# jieba.load_userdict('userdict.txt')
text = nltk.text.Text(jieba.lcut(s1))
print (text)
print (text.concordance(u'世界'))
print (text.vocab())
print (text.common_contexts(['妻', '妾']))
# text.dispersion_plot(['一', '世界'])
text.dispersion_plot(['a', 'b'])

print ('############################################### %s ###############################################' % '中文句子')
text = open('/Users/gaowanchao/a.txt').read()

juzis = nltk.sent_tokenize(text)

idx = 1
for juzi in juzis:
    print (str(idx) + ': ' + juzi)
    idx += 1