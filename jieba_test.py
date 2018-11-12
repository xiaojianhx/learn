#!/usr/bin/python3
# encoding: utf-8

import jieba
import jieba.analyse

def test():
    text = '真是好久好久没来哈皮娜拉野生动物园了，记忆里还是小时候三四年级学校组织春游去的银河系'

    str1 = jieba.cut(text, cut_all=True)
    print ('全模式分词：', '|'.join(str1))

    str2 = jieba.cut(text, cut_all=True, HMM=False)
    print ('全模式分词：', '|'.join(str2))

    str3 = jieba.cut(text, cut_all=False)
    print ('全模式分词：', '|'.join(str3))

    str4 = jieba.cut(text, cut_all=False, HMM=False)
    print ('全模式分词：', '|'.join(stu3000r4))

    str5 = jieba.cut_for_search(text)
    print ('搜索引擎模式分词：', '|'.join(str5))

    str6 = jieba.analyse.extract_tags(text)
    print ('关键词：', '|'.join(str6))

    str7 = jieba.analyse.extract_tags(text, topK=3)
    print ('关键词：', '|'.join(str7))


    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))

# jieba.set_dictionary('/Users/gaowanchao/b.txt')

def load_stop_words(filepath):

    fr = open(filepath, 'r', encoding='utf8')
    stop_words = []
    for line in fr:
        stop_words.append(line.strip())
    fr.close()

    return stop_words


def find_new_vocabulary(text):

    stop_words = load_stop_words('data/stop_words.txt')

    jieba.load_userdict('data/userdict.txt')
    words = jieba.cut(text, cut_all=False)
    word_freq = {}

    for word in words:

        if word in stop_words:
            continue

        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    freq_word = []

    for w, f in word_freq.items():
        freq_word.append((w, f))

    freq_word.sort(key = lambda x: x[1], reverse=True)

    userdict = {}

    fr = open('data/userdict.txt', 'r')

    for line in fr:
        line = line.split(' ')
        try:
            userdict[line[0]] = line[1]
        except Exception as e:
            print ('error:', line)

    fr.close()

    fw = open('data/userdict.txt', 'w')

    for w, f in freq_word:

        if w in userdict.keys():
            userdict[w] = int(userdict[w]) + int(f)
        else:
            userdict[w] = f

    userdict = sorted(userdict.items(), reverse=True)
    print (userdict)

    for k, v in userdict:
        fw.write('%s %s \n' % (k, v))
    fw.close()
    return freq_word

print ('-------------------------------------------------------------------------------------')

text = open('/Users/gaowanchao/a.txt').read()

freq_word = find_new_vocabulary(text)

print (freq_word)