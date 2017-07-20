#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: muyeby
@contact: bxf_hit@163.com
@site: http://muyeby.github.io
@software: PyCharm
@file: Predeal.py
@time: 17-4-5 下午3:23
"""
import argparse
from nltk.corpus import stopwords
import json

wordCountDir = ""
originWordVec = ""
OutPutDir = ""

def Predeal(originFile,wordCountFile,lang,filters,newFile,cntFile,threshold):
    wordDict = {}
    wordDict2 = {}
    for line in open(wordCountFile):
        if len(line.strip().split(':'))==2:
            key,value = line.strip().split(':')
            wordDict[key]=int(value)
    file1 = open(originFile, 'rb')
    file2 = open(newFile, 'wb')
    cntFile= open(cntFile,'wb')
    stopword=[]
    if(filters==1):
        if(lang=="zh"):
            for line in open("vocab.zh",'r'):
                word = line.strip()
                stopword.append(word)
        if(lang=="en"):
            stopword = set(stopwords.words('english'))
    i=0
    if (file1):
	print "start generate new vector file...\n"
        #print filters
        for line in file1:
            if i!=0:
                tmp = line.strip().split(' ')
	        word = tmp[0]
                if (wordDict.has_key(tmp[0]) and wordDict[tmp[0]]>threshold):
                    if(lang== "zh" and filters==1 and word not in stopword):
                        continue
                    ttmp = line.strip()+"\n"
                    ttmp2 = word+" "+str(wordDict[tmp[0]])+"\n"
                    file2.write(ttmp)
                    cntFile.write(ttmp2)
            i+=1
    else:
        print "Failed to open"
    file1.close()
    file2.close()
    cntFile.close()
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w1", "--originFile", type=str, help="Origin Vector file")
    parser.add_argument("-w2", "--wordCountFile", type=str, help="Word Count file")
    parser.add_argument("-o", "--outputfile", type=str, help="Output file for predealed vectors")
    parser.add_argument("-o2", "--countfile", type=str, help="word count file for predealed vectors")
    parser.add_argument("-lang","--language", type=str, help="language")
    parser.add_argument("-ft", "--filters", type=int, help="whether filter stopwords")
    parser.add_argument("-th", "--threshold", type=int, help="threshold wordcounts")
    args = parser.parse_args()
    print "Do some predeal works\n"
    Predeal(args.originFile,args.wordCountFile,args.language,args.filters,args.outputfile,args.countfile,args.threshold)
