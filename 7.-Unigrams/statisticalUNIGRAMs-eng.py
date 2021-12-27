from TBXTools import *
extractor=TBXTools()

print("NO SELECTION\n")

extractor.create_project("statistical1UNINOSEL.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-eng.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor.ngram_calculation(nmin=1,nmax=1)
extractor.load_sl_stopwords("stop-eng.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-UNINOSEL-eng.txt")
extractor.load_evaluation_terms("corp_en_terms_nes.ann",nmin=1,nmax=1)

for position in [100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position)
    #print("%5i %7.3f %5i %7.3f %7.3f %7.3f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
    cadena=str(position)+" & "+str(round(eval[3],2))+" & "+str(round(eval[4],2))+" & "+str(round(eval[5],2))+"\\\\"
    print(cadena)

print("UNIGRAM SELECTION\n")

extractor2=TBXTools()
extractor2.create_project("statistical1UNISEL.sqlite","eng",overwrite=True)
extractor2.load_sl_corpus("corpus-eng.txt")
extractor2.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor2.ngram_calculation(nmin=2,nmax=3)
extractor2.load_sl_stopwords("stop-eng.txt")
extractor2.statistical_term_extraction()
extractor2.select_unigrams("unigrams.txt",position=-1)
extractor2.select_unigrams("unigrams.txt",position=0)
extractor2.save_term_candidates("candidates-UNISEL-eng.txt")
extractor2.load_evaluation_terms("corp_en_terms_nes.ann",nmin=1,nmax=1)

for position in [100,200,500,1000,2000]:
    eval=extractor2.evaluate_pos(position)
    #print("%5i %7.3f %5i %7.3f %7.3f %7.3f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
    cadena=str(position)+" & "+str(round(eval[3],2))+" & "+str(round(eval[4],2))+" & "+str(round(eval[5],2))+"\\\\"
    print(cadena)
 
