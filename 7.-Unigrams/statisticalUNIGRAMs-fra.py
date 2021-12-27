from TBXTools import *
extractor=TBXTools()


print("NO SELECTION\n")

extractor.create_project("statistical1UNINOSEL-fra.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor.ngram_calculation(nmin=1,nmax=1)
extractor.load_sl_stopwords("stop-fra.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-UNINOSEL-fra.txt")
extractor.load_evaluation_terms("corp_fr_terms_nes.ann",nmin=1,nmax=1)

for position in [100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position)
    #print("%5i %7.3f %5i %7.3f %7.3f %7.3f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
    cadena=str(position)+" & "+str(round(eval[3],2))+" & "+str(round(eval[4],2))+" & "+str(round(eval[5],2))+"\\\\"
    print(cadena)

print("UNIGRAM SELECTION\n")

extractor2=TBXTools()
extractor2.create_project("statistical1UNISEL-fra.sqlite","eng",overwrite=True)
extractor2.load_sl_corpus("corpus-fra.txt")
extractor2.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor2.ngram_calculation(nmin=2,nmax=3)
extractor2.load_sl_stopwords("stop-fra.txt")
extractor2.statistical_term_extraction()
extractor2.select_unigrams("unigrams.txt",position=-1)
extractor2.select_unigrams("unigrams.txt",position=0)
extractor2.save_term_candidates("candidates-UNISEL-fra.txt")
extractor2.load_evaluation_terms("corp_fr_terms_nes.ann",nmin=1,nmax=1)

for position in [100,200,500,1000,2000]:
    eval=extractor2.evaluate_pos(position)
    #print("%5i %7.3f %5i %7.3f %7.3f %7.3f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
    cadena=str(position)+" & "+str(round(eval[3],2))+" & "+str(round(eval[4],2))+" & "+str(round(eval[5],2))+"\\\\"
    print(cadena)
 
