from TBXTools import *

extractor=TBXTools()
extractor.create_project("project-linguistic-eng","eng",overwrite=True)
extractor.load_POS_model("en_core_web_sm")
extractor.load_sl_corpus("corpus-eng.txt")
extractor.tag_spacy()
extractor.save_sl_tagged_corpus("corpus-tagged-spacy-eng.txt")
