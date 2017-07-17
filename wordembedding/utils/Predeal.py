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

wordCountDir = ""
originWordVec = ""
OutPutDir = ""

def Predeal(originFile,wordCountFile,newFile,cntFile):
    wordDict = {}
    wordDict2 = {}
    for line in open(wordCountFile):
        if len(line.strip().split(':'))==2:
            key,value = line.strip().split(':')
            wordDict[key]=int(value)
    file1 = open(originFile, 'rb')
    file2 = open(newFile, 'wb')
    cntFile= open(cntFile,'wb')
    i=0
    if (file1):
	print "start generate new vector file...\n"
        for line in file1:
            if i!=0:
                tmp = line.strip().split(' ')
	        word = tmp[0]
                if (wordDict.has_key(tmp[0]) and wordDict[tmp[0]]>1000):
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

    args = parser.parse_args()
    print "Do some predeal works\n"
    Predeal(args.originFile,args.wordCountFile,args.outputfile,args.countfile)
