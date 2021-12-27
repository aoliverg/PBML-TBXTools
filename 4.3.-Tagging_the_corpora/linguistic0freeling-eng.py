from TBXTools import *

freelingpath="/usr/local/share/freeling"
extractor=TBXTools()
extractor.create_project("project-linguistic-eng","eng",overwrite=True)
extractor.load_sl_corpus("corpus-eng.txt")
extractor.start_freeling_api(freelingpath,"en")
extractor.tag_freeling_api()
extractor.save_sl_tagged_corpus("corpus-tagged-freeling-eng.txt")
