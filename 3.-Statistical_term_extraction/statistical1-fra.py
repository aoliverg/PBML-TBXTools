from TBXTools import *
extractor=TBXTools()
extractor.create_project("statistical-fra.sqlite","fra",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor.ngram_calculation(nmin=2,nmax=3)
extractor.load_sl_stopwords("stop-fra.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-stat-fra.txt")
