from TBXTools import *

freelingpath="/usr/local/share/freeling"
extractor=TBXTools()
extractor.create_project("project-linguistic-fra","fra",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.start_freeling_api(freelingpath,"fr")
extractor.tag_freeling_api()
extractor.save_sl_tagged_corpus("corpus-tagged-freeling-fra.txt")
