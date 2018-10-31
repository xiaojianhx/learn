#!/usr/bin/python3
# encoding: utf-8
import nltk
import jieba.analyse
import jieba.posseg

from nltk.corpus import treebank
t = treebank.parsed_sents('/Users/gaowanchao/a.txt')[0]
t.draw()

s = '金庸逝世！江湖再无金大侠，只剩沧海一声笑……'
s = '其实大家买手机就是看个心情，没必要比来比去的。'
s = '其实 大家买手机'

words = jieba.posseg.cut(s)

l = []
# l.append('S')
for word, f in words:
    print (word, ' --> ', f)

    l.append(word)

g = '''
    S -> D VN
    D -> '其实' | '就是' | '必要'
    VN -> NN
    N -> '大家' | '买手机' | '心情'
    v -> '看' | '没'
    l -> '个' | '比来比去'
    x -> '，' | '。'
    uj -> '的'
'''


g1 = '''
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked" | '爱'
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | '我' | '你'
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    P -> "in" | "on" | "by" | "with"
'''


s1 = '我 爱 你'
l1 = list(s.split())

grammar1 = nltk.CFG.fromstring(g)

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(l):
    print(tree)
 
tree.draw()