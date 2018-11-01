#!/usr/bin/python3
# encoding: utf-8
import nltk
import jieba.analyse
import jieba.posseg
# jieba.load_userdict('userdict.txt')

s = '金庸逝世！江湖再无金大侠，只剩沧海一声笑……'
s = '其实大家买手机就是看个心情，没必要比来比去的。'
s = '因为你不好，所以我不喜欢你。'

words = jieba.posseg.cut(s)

l = []
# l.append('S')
for word, f in words:
    print (word, ' --> ', f)

    l.append(word)

g = '''
    S -> D NN DVLN X VD L UJ X
    NN -> N N
    DVLN -> D V L N
    VD  -> V D
    D -> '其实' | '就是' | '必要'
    N -> '大家' | '买手机' | '心情'
    V -> '看' | '没'
    L -> '个' | '比来比去'
    X -> '，' | '。'
    UJ -> '的'
'''

g = '''
    s -> c rd x c rdvr x
    rd -> r d
    rdvr -> r d v r
    c -> '因为' | '所以'
    d -> '不' | '不好'
    r -> '我' | '你'
    v -> '喜欢'
    x -> '，' | '。'
'''

grammar1 = nltk.CFG.fromstring(g)

rd_parser = nltk.RecursiveDescentParser(grammar1)

for tree in rd_parser.parse(l):
    print(tree)
    print ('\n'.join(dir(tree)))

# print (tree['c'])
# tree.reverse()
# tree.sort()

ge = nltk.parse.generate(grammar1)
print (ge.generate())


print ('-----------------------------')
for t in tree:
    print (t.label())
# tree.draw()
