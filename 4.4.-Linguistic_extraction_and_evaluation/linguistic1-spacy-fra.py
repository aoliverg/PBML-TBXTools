from TBXTools import *

extractor=TBXTools()
extractor.create_project("linguistic1.sqlite","fra",overwrite=True)
extractor.load_sl_tagged_corpus("corpus-tagged-spacy-fra.txt")
extractor.load_linguistic_patterns("POS-patterns-spacy-fra.txt")
extractor.tagged_ngram_calculation(nmin=1,nmax=3,minfreq=2)
extractor.linguistic_term_extraction(minfreq=2)
extractor.save_term_candidates("candidates-linguistic-spacy-fra.txt",minfreq=2)
extractor.load_evaluation_terms("corp_fr_terms_nes.ann")

for position in [100,200,500,1000,2000]:
    eval=extractor.evaluate_pos(position)
    print("%5i %7.2f %5i %7.2f %7.2f %7.2f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5]))
