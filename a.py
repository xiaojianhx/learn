import spacy

import nltk

text = '''
近日，香港著名影星蓝洁瑛去世，年仅55岁。这对于喜爱她的观众和粉丝来说无疑是一个巨大的打击，要知道蓝洁瑛当年盛极一时的名气和人气都是大家有目共睹的，即使后来被雪藏依旧是很多人心中的绝对的女神，而后来被曝光精神状况不佳后，虽然时有新闻爆出却仍然是无尽悲凉，令人唏嘘不已。
'''

text1 = '''
    London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium.
'''

# 句子分割
import re
sentences = re.split('(。|！|\!|\.|？|\?)', text)

# 词汇标记法
import jieba
import jieba.posseg
for sentence in sentences:
    print (sentence)

    for tmp, f in jieba.posseg.cut(sentence):
        print (' >>>> ', tmp, ' --> ', f)

exit()



nlp = spacy.load('en_core_web_lg')

text = '''
    London is the capital and most populous city of England and 
the United Kingdom.  Standing on the River Thames in the south east 
of the island of Great Britain, London has been a major settlement 
for two millennia. It was founded by the Romans, who named it Londinium.
'''

text = '''
    伦敦是英国的首都。我们都爱她。
'''

doc = nlp(text)

for entity in doc.ents:
    print (f"{entity.text} ({entity.label_})")