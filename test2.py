#!/usr/bin/python3
# encoding: utf-8


from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import jieba

text = open('/Users/gaowanchao/a.txt').read()
text = nltk.text.Text(jieba.lcut(text))


print (text.concordance('马塞洛'))
clean_tokens = list()
# sr = stopwords.words('english')

tokens = nltk.word_tokenize(text)
for token in tokens:
    # if not token in sr:
    clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)