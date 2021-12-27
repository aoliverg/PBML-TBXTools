from TBXTools import *

extractor=TBXTools()
extractor.create_project("project-linguistic-fra","fra",overwrite=True)
extractor.load_POS_model("fr_core_news_sm")
extractor.load_sl_corpus("corpus-fra.txt")
extractor.tag_spacy()
extractor.save_sl_tagged_corpus("corpus-tagged-spacy-fra.txt")
