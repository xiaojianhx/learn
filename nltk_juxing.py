#!/usr/bin/python3
# encoding: utf-8
import nltk

def dump_result(result):
    for item in result:
        print (item[0],",",item[1])
    print
    

grammar1 = nltk.CFG.fromstring('''
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked" | '爱'
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | '我' | '你'
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    P -> "in" | "on" | "by" | "with"
''')


s = '我 爱 你'

tokens = nltk.word_tokenize(s)

from nltk.corpus import sinica_treebank

sinica_treebank_tagged_sents = sinica_treebank.tagged_sents()   # 以句为单位标
size = int(len(sinica_treebank_tagged_sents) * 0.9)
train_sents = sinica_treebank_tagged_sents[:size]   # 90% 数据作为训练集
test_sents = sinica_treebank_tagged_sents[size:]    # 10% 数据作为测试集
 
t0 = nltk.DefaultTagger('Nab')  # 词性的默认值为名词
t1 = nltk.UnigramTagger(train_sents, backoff = t0)    # 一元标注
t2 = nltk.BigramTagger(train_sents, backoff = t1) # 多元（二元）标注
 
dump_result(t2.tag(tokens))
print (t2.evaluate(test_sents))   # 根据带标注的文本，评估标注器的正确率

exit()
tag = nltk.pos_tag(tokens)

for i in tag:
    print (i)

sent = s.split()

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(sent):
    print(tree)
 
# tree.draw()