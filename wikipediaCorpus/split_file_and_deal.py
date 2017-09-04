from multiprocessing import Process

num_of_p = 16 
# zh =======================
# cmd = 'java -mx5000m -classpath /home/xfbai/tools/stanford-postagger-full-2017-06-09/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model /home/xfbai/tools/stanford-postagger-full-2017-06-09/models/chinese-distsim.tagger -textFile {} >{}'
# en =======================
# cmd = 'java -mx5000m -classpath /home/xfbai/tools/stanford-postagger-full-2017-06-09/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model /home/xfbai/tools/stanford-postagger-full-2017-06-09/models/wsj-0-18-left3words-distsim.tagger -textFile {} >{}'
#cmd = 'java -mx5000m -classpath /home/xfbai/tools/stanford-postagger-full-2017-06-09/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model /home/xfbai/tools/stanford-postagger-full-2017-06-09/models/english-left3words-distsim.tagger -textFile {} >{}'
cmd = '/home/xfbai/tools/THULAC/thulac -seg_only -model_dir /home/xfbai/tools/THULAC/models -input {} -output {}'
#cmd = '/home/xfbai/tools/THULAC/thulac -model_dir /home/xfbai/tools/THULAC/models -input {} -output {}'
def deal(filename,outputname):
    import os
    os.system(cmd.format(filename,outputname))

    return 0
import sys

origin_file = sys.argv[1]
with open(origin_file) as f:
	lines = f.readlines()
lines = filter(lambda x:not x.strip()=='',lines)
fsize = len(lines)/num_of_p +1


filename_template = 'final_zh_input_{}'
#filename_template = 'final_en_input_{}'

for i in range(num_of_p):
    with open(filename_template.format(i),'w') as f:
        for j in range(fsize):
            try:
                f.write(lines[i*fsize+j])
            except:
                break
		

outputname_template = 'final_zh_out_{}'
#outputname_template = 'final_en_out_{}'

#p_list= [Process(target=deal, args=[filename_template.format(i),outputname_template.format(i)]) for i in range(num_of_p)]
p_list= [Process(target=deal, args=[filename_template.format(i),outputname_template.format(i)]) for i in range(num_of_p)]

map(lambda x:x.start(),p_list)

map(lambda x:x.join(),p_list)
