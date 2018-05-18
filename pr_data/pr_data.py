#!/usr/bin/python
# -*- coding:utf-8 -*-


__author__ = 'luhui.liu'


from collections import Counter
#import jieba
import codecs
from tqdm import tqdm
import re


filepath = "../train_data/nlpcc-iccpol-2016.dbqa.training-data"
targetFile = "../train_data/nlpcc-iccpol-2016.dbqa.training-data_split_stop"


# @see 读取文件内容
def readFile(filename):
    content = ""
    try:
        fo = codecs.open(filename, 'r', "utf-8")
        print("读取文件名：", filename)

        for line in fo.readlines():
            content += line
        print("字数：", len(content))

    except IOError as e:
        print("文件不存在或者文件读取失败")

        return ""
    else:
        fo.close()
        # re_han.split(sentence)
        return content


# @see 写入文件内容（数组会使用writelines进行写入）codec.open实现
# @param toFile 文件名
#        content 内容
def writeFile(toFile, content):
    try:
        fo = codecs.open(toFile, 'wb', "utf-8")
        print("文件名：", toFile)

        if type(content) == type([]):
            fo.writelines(content)
        else:
            fo.write(content)
    except IOError:
        print("没有找到文件或文件读取失败")

    else:
        print("文件写入成功")
        fo.close()
# jieba.load_userdict('userdict.txt')  
# 创建停用词list  
def get_stop_words(filepath):
    """
    load stop words
    :param filepath:
    :return:
    """
    filepath = "./pr_data/stop_word.dat"
    fr = codecs.open(filepath, 'r', 'utf-8')
    stopwords = [line.strip() for line in fr.readlines()]
    return stopwords  


def tokenzier(text):
    """
    jieba tokenzier，default not use stop_words
    :param rawContent: sentence
    :return: target content
    """

    stop_words = []
    # use stop_words
    #stop_words = get_stop_words()
    # text = re.sub("[\s+\.\!\/_,:{}()<>?[]\;$%^*(+\"\']+|[+——！，。？：‘’”“【】{}（）《》；·～〈〉-`、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), text.decode('utf8'))
    #parallel model ,parallel number is 4
    jieba.enable_parallel(4)
    #disable parallel tokenzier
    # jieba.disable_parallel()
    text_list = [x.strip() for x in list(jieba.cut(text.strip(), cut_all=False)) if x not in stop_words and x != ""]
    output = " ".join(text_list)
    #text = re.sub("[A-Za-z]+", "ENG", text)
    #text = re.sub("[0-9.]+", "NUM", text)
    return output


def count_tf(rawContent):
    fileout_path="../data2/result.txt"
    wlist = rawContent.split()  # 将分词结果按空格切割为列表（字符串的切割）
    num_dict = Counter(wlist)  # 统计词频

    # 统计结果写入result.txt(字典的遍历)
    for (k, v) in num_dict.items():
        codecs.open(fileout_path, 'a+', "utf-8").write(str(k) + ' ' + str(v) + '\n')   # 将k，v转换为str类型


if __name__ == '__main__':
    #结巴分词
    # output_content = readFile(filepath)
    # writeFile(targetFile,output_content)
    # count_tf("你好 北京 北京")
    for i in range(10):
        print(i)

