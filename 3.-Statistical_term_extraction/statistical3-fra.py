from TBXTools import *
extractor=TBXTools()
extractor.create_project("statistical1.sqlite","fra",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor.ngram_calculation(nmin=2,nmax=3)
extractor.load_sl_stopwords("stop-fra.txt")
extractor.load_sl_inner_stopwords("inner-stop-fra.txt")
extractor.statistical_term_extraction()
extractor.case_normalization(verbose=True)
extractor.nest_normalization(verbose=True)
extractor.load_sl_exclusion_regexps("regexps.txt")
extractor.regexp_exclusion(verbose=True)
extractor.save_term_candidates("candidates-stat-fra.txt")
extractor.load_evaluation_terms("corp_fr_terms_nes.ann")

for position in [100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position)
    print("%5i %7.2f %5i %7.2f %7.2f %7.2f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
 
