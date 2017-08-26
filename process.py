# -*- coding: utf-8 -*-

from collections import Counter
import json
import argparse

def posTaggerCnt(data,output):
    tagger = Counter()
    for line in open(data,'r'):
        words = line.strip().split(' ')
        tagger.update(words)
    
    jsObj = json.dumps(tagger)
    fileObj = open(output,'w')
    fileObj.write(jsObj)
    fileObj.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w1", "--originFile", type=str, help="Origin Vector file")
    parser.add_argument("-o", "--outputfile", type=str, help="Output file for predealed vectors")
    args = parser.parse_args()
    print "Do some predeal works\n"
    posTaggerCnt(args.originFile,args.outputfile)
