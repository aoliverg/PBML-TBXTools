from TBXTools import *
extractor=TBXTools()
extractor.create_project("statistical-eng.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-eng.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor.ngram_calculation(nmin=2,nmax=3)
extractor.load_sl_stopwords("stop-eng.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-stat-eng.txt")
