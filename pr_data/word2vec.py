#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'luhui.liu'

from gensim.models import word2vec
# 停止词
from nltk.corpus import stopwords


# # 用生成器的方式读取文件里的句子# 适合读取大容量文件，而不用加载到内存class MySentences(object):
# def __init__(self, fname):
#     self.fname = fname
#     def __iter__(self):
#         for line in open(self.fname,'r'):
#             yield line.split()


def removeStopWords(sentences):
    """
    去除停用词
    :param sentences: 去除停用词之前的句子
    :return: 去除停用词之后的句子
    """
    sentences_list = list(sentences)
    StopWords = stopwords.words('english')
    for idx, sentence in enumerate(sentences_list):
        sentence = [w for w in sentence if w not in StopWords]
        sentences_list[idx] = sentence
    return sentences_list


def w2vTrain(f_input, model_output_path):
    """
    word2vec模型训练函数
    :param f_input: 完成分词后的语料库
    :param model_output: 生成路径
    :return: 在model_output_path 生成model文件和word2vec.txt格式化后的文件
    """
    print('Start...')
    sentences = word2vec.Text8Corpus(f_input)
    # 去除停用词，可选
    # sentences = removeStopWords(sentences)

    # 第一个参数是训练语料，第二个参数是小于该数的单词会被剔除，默认值为5, 第三个参数是神经网络的隐藏层单元数，默认为100
    model = word2vec.Word2Vec(sentences, min_count=3, size=50, window=5, workers=multiprocessing.cpu_count())

    y2 = model.similarity(u"不错", u"好吃")  # 计算两个词之间的余弦距离
    print(y2)

    for i in model.most_similar(u"好吃"):  # 计算余弦距离最接近“滋润”的10个词
        print(i[0], i[1])

    # 存储训练好的模型：
    if saved:
        model.save(model_output_path + "model")
        model.wv.save_word2vec_format(model_output_path + "word2vec.txt", binary=False)
    print("Finished!")

def wordsimilarity(word, model):
    """
    单词相似度查看
    :param word: 输入的单词
    :param model: 训练好的模型
    """
    semi = ''
    try:
        semi = model.most_similar(word, topn=10)
    except KeyError:
        print('The word not in vocabulary!')
    for term in semi:
        print('%s,%s' % (term[0],term[1]))

if __name__ == '__main__':
    f_input = '../output/wiki_chs.split'
    model_output_path = '../output/'
    # 加载模型
    w2v_model = word2vec.Word2Vec.load(model_output_path + 'model')
    # 查看body的相似词
    w2v_model.most_similar('body')
    # 获取每个词的词向量
    w2v_model.model['computer']
