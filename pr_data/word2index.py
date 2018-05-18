#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'luhui.liu'

import codecs
import tqdm

def load_vocab(vocab_filepath):
    vocab2idx = {}

    for line in open(vocab_filepath):
        ps = line.split('\t')
        if int(ps[1]) < 5:
            continue
        vocab2idx[ps[0]] = ps[1]
    print("success")
    return vocab2idx


def word2Index_wiki(vocab_filepath):
    """
    去除wiki中不存在的词
    :param vocab_filepath:原词词词频文件
    :return:
    """
    #维基百科路径
    wiki_filepath = "../output1/word2vec.txt"
    #去除wiki中不包含后保存的新词频文件
    out_vocab_filepath = "../train_data/vocab_new"
    #去除不包含的word2index文件
    vocab_index_filepath = "../train_data/vocab_idx"
    idx = 0
    vocab2idx = load_vocab(vocab_filepath)
    wf = codecs.open(vocab_index_filepath, 'w', "utf-8")
    wf_new = codecs.open(out_vocab_filepath, 'w', "utf-8")
    with codecs.open(wiki_filepath,'w', "utf-8") as fin:
        next(fin)
        for line in tqdm(fin.readlines()):
            ps = line.rstrip().split()
            if ps[0] in vocab2idx:
                wf.write(ps[0] + ' ' + str(idx) + '\n')
                wf_new.write(ps[0] + ' ' + str(vocab2idx[ps[1]]) + '\n')
                idx += 1

    print("success")


def word2index(count_file):
    """
    普通的word2index
    :param count_file: 词频文件
    :return:
    """
    out_filepath = "../train_data/vocab_idx_n"
    vocab2idx = {}
    idx = 0
    wf = codecs.open(out_filepath, 'w', "utf-8")
    for line in open(count_file):
        ps = line.split(' ')
        if int(ps[1]) < 5:
            continue
        wf.write(ps[0] + ' ' + str(idx) + '\n')
        idx += 1
    print("success")


def train2index():
    targetFile = "../train_data/nlpcc-iccpol-2016.dbqa.training-data_split_stop"
    targetFile_a = "../train_data/nlpcc-iccpol-2016.dbqa.training-data_idx"
    voca = "../train_data/vocab_idx"
    dict = {}
    # 从分词后的源文件中读取数据
    fo = codecs.open(voca, 'r', "utf-8")
    for line in fo.readlines():
        ps = line.split(' ')
        dict[ps[0]] = ps[1]

        # 词语数组
    wordList = []
    # 用于统计词频
    wordCount = {}

    fi = codecs.open(targetFile, 'r', "utf-8")
    wf = codecs.open(targetFile_a, 'w', "utf-8")
    for item in tqdm(fi.readlines()):
        string = item.strip()

        psItem = string.split('\t')

        qLists = psItem[0].strip().split(' ')

        qstring = ""
        for q in qLists:
            if q == '':
                continue
            if q in dict:
                qstring = qstring + dict[q].strip() + ' '
        aList = psItem[1].strip().split(' ')
        astring = ""
        for a in aList:
            if a in dict:
                astring += dict[a].strip() + ' '
        if qstring == '' or astring == '':
            continue
        wf.write(qstring.strip() + '\t' + astring.strip() + '\t' + psItem[2].strip() + '\n')
    print("success")

# vocab2idx=load_vocab()
# load_word2vec(vocab2idx)
if __name__ == '__main__':
    #word2index("..")
    import re
    string  = "("
    re_han = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+——！【】”“‘’，。？、~@#￥%……&*（）]+",re.U)
    if re_han.match(string):
        print("111")
    string1 = "你好，我是  刘\n nihao"
    for i in string1.split(" "):
        print(i)
