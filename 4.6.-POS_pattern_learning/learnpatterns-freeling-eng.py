from TBXTools import *

extractor=TBXTools()
extractor.create_project("learnpatterns-eng.sqlite","eng",overwrite=True)
extractor.load_sl_tagged_corpus("corpus-tagged-freeling-eng.txt")
extractor.load_evaluation_terms("ref-terms-train-eng.txt",nmin=1,nmax=3)
extractor.tagged_ngram_calculation(nmin=2,nmax=3,minfreq=1)
extractor.learn_linguistic_patterns("learnt-patterns-freeling-eng.txt",representativity=95, showfrequencies=True)
