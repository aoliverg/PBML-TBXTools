from TBXTools import *
extractor=TBXTools()
extractor.create_project("statistical.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-eng.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor.ngram_calculation(nmin=2,nmax=3)
extractor.load_sl_stopwords("stop-eng.txt")
extractor.load_sl_inner_stopwords("inner-stop-eng.txt")
extractor.statistical_term_extraction()
extractor.case_normalization(verbose=True)
extractor.nest_normalization(verbose=True)
extractor.load_sl_exclusion_regexps("regexps.txt")
extractor.regexp_exclusion(verbose=True)
extractor.save_term_candidates("candidates-stat-eng.txt")
extractor.load_evaluation_terms("corp_en_terms_nes.ann")

for position in [100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position)
    print("%5i %7.2f %5i %7.2f %7.2f %7.2f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
 
