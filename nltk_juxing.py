#!/usr/bin/python3
# encoding: utf-8
import nltk
import jieba

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
sent = s.split()

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(sent):
    print(tree)
 
tree.draw()