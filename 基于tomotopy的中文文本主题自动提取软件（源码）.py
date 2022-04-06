#-*- coding:utf-8 -*-

import pandas as pd
import csv
import re
import jieba
from cntext import STOPWORDS_zh
import tomotopy as tp
from harvesttext import HarvestText
import os
Path=os.getcwd()

#读取数据
train_path=Path+"\\input.csv"
data = pd.read_csv(train_path)
def extract_only_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
#导出清理后的详细文本
vector = open(Path+'\\清理后的详细文本.txt', 'w',encoding='utf-8')
for text in data['text']:
    ht0 = HarvestText()
    cleaned_text=ht0.clean_text(text, t2s=True)
    cleaned_text= extract_only_chinese(cleaned_text)
    #print(cleaned_text)
    vector = open(Path+'\\清理后的详细文本.txt', 'a',encoding='utf-8')
    vector.write(str(cleaned_text))
    vector.write('\n')
    vector.close()
#读取清理后的详细文本
f=open(Path+"\\清理后的详细文本.txt", encoding='utf-8')
txt=[]
for line in f:
    txt.append(line.strip())
data = pd.DataFrame({
    "text":txt,
})
#预览前5条数据
print(data[:5])

#中文分词
def segment(text):
    words = jieba.lcut(text)
    words = [w for w in words if w not in STOPWORDS_zh]
    return words
data['words'] = data['text'].apply(segment)
data.head()

#自动寻找最优主题值和输出主题一致性
def find_k(docs, min_k=1, max_k=20, min_df=2):
    # min_df 词语最少出现在2个文档中
    import matplotlib.pyplot as plt
    scores = []
    for k in range(min_k, max_k):
        # seed随机种子，保证运行结果保持一致
        mdl = tp.LDAModel(min_df=min_df, k=k, seed=42)
        for words in docs:
            if words:
                mdl.add_doc(words)
        mdl.train(20)
        coh = tp.coherence.Coherence(mdl)
        scores.append(coh.get_score())

    scores = [round(x, 2) for x in scores]
    topic_coherence = pd.DataFrame({
        "num":range(min_k, max_k),
        "coherence":scores
    })
    print('主题一致性'+'\n',topic_coherence)
    topic_coherence = topic_coherence.sort_values('coherence', ascending=False)
    #print(topic_coherence)
    #本程序默认设置主题数不小于2
    max_2=topic_coherence.loc[(topic_coherence["num"] > 2)]
    max_2_num=max_2.iloc[[0],[0]].values[0][0]
    print('最佳主题数为：',max_2_num)
    return max_2_num
k_best=find_k(docs=data['words'], min_k=1, max_k=10, min_df=2)
#print(k_best)

#初始化LDA
mdl = tp.LDAModel(k=k_best, min_df=2, seed=42)
for words in data['words']:
    #确认words 是 非空词语列表
    if words:
        mdl.add_doc(words=words)

#训练
mdl.train()

#导出每个主题的特征词
topic_word = open(Path + '\\主题词.txt', 'w')
for k in range(mdl.k):
    result=mdl.get_topic_words(k, top_n=20)
    topic_word = open(Path + '\\主题词.txt', 'a')
    topic_word.write('Top 10 words of topic #{}'.format(k))
    topic_word.write(str(result))
    topic_word.write('\n')
    topic_word.close()

#导出每个文档的主题值
vector = open(Path+'\\主题值.csv', 'w')
for word in data['words']:
    doc_inst = mdl.make_doc(words=word)
    topic_dist, ll = mdl.infer(doc_inst)
    #print("Topic Distribution for Unseen Docs: ", topic_dist)
    vector = open(Path+'\\主题值.csv', 'a')
    vector.write(str(topic_dist))
    vector.write('\n')
    vector.close()