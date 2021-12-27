from TBXTools import *
from collections import defaultdict
import codecs


total={}
correct={}
precision={}
recall={}
f1={}

extractor=TBXTools()
extractor.create_project("statistical1.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-eng.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor.ngram_calculation(nmin=3,nmax=3)
extractor.load_sl_stopwords("stop-eng.txt")
extractor.statistical_term_extraction()

extractor.save_term_candidates("candidates-stat-eng.txt")

extractor.load_evaluation_terms("ref-terms-test-eng.txt",nmin=3,nmax=3)
extractor.load_tsr_terms("ref-terms-train-eng.txt",nmin=2,nmax=5)

total={}
correct={}
precision={}
recall={}
f1={}


measure="raw_freq"
total[measure]={}
correct[measure]={}
precision[measure]={}
recall[measure]={}
f1[measure]={}
for position in [10,50,100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position,order="desc")
    total[measure][position]=eval[2]
    correct[measure][position]=eval[1]
    precision[measure][position]=eval[3]
    recall[measure][position]=eval[4]
    f1[measure][position]=eval[5] 



#extractor.load_tsr_terms("corp_en_terms_nes-bigrams.ann",nmin=2,nmax=2)

extractor.tsr()

measure="TSR"
total[measure]={}
correct[measure]={}
precision[measure]={}
recall[measure]={}
f1[measure]={}
for position in [10,50,100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position,order="desc")
    total[measure][position]=eval[2]
    correct[measure][position]=eval[1]
    precision[measure][position]=eval[3]
    recall[measure][position]=eval[4]
    f1[measure][position]=eval[5]


for position in [10,50,100,200,500,1000,2000]:
    cadena=str(position)+" & "+str(round(precision["raw_freq"][position],2))+" & "+str(round(f1["raw_freq"][position],2))+" & "+str(round(precision["TSR"][position],2))+" & "+str(round(f1["TSR"][position],2))
    print(cadena)