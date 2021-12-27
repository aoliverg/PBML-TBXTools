from TBXTools import *
from collections import defaultdict

sortida=codecs.open("table-statistical-bigrams.txt","w",encoding="utf-8")

total={}
correct={}
precision={}
recall={}
f1={}

extractor=TBXTools()
extractor.create_project("statistical1.sqlite","eng",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor.ngram_calculation(nmin=2,nmax=2)
extractor.load_sl_stopwords("stop-fra.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-stat-fra.txt")
extractor.load_evaluation_terms("corp_fr_terms_nes-bigrams.ann")

measures=[("raw_freq","desc"),("poisson_stirling_2g","desc"),("t_score_2g","desc"),("chi_sq_2g","asc"),("log_likelihood_ratio","desc"),("odds_2g","asc"),("MI","asc"),("dice_2g","asc"),("jaccard_2g","asc"),("phi_sq_2g","asc"),("pmi","asc")]
for measureorder in measures:
    measure=measureorder[0]
    total[measure]={}
    correct[measure]={}
    precision[measure]={}
    recall[measure]={}
    f1[measure]={}
    order=measureorder[1]
    print("Measure: ",measure)
    print("ORDER: ", order)
    extractor.association_measures(measure=measure)
    print("limit correct total precision, recall, F1")
    for position in [10,50,100,200,500,1000,2000]:
        eval=extractor.evaluate_pos(position,order=order)
        #print("%5i %7.3f %5i %7.3f %7.3f %7.3f" % (eval[0], eval[1], eval[2], eval[3], eval[4], eval[5])) 
        total[measure][position]=eval[2]
        correct[measure][position]=eval[1]
        precision[measure][position]=eval[3]
        recall[measure][position]=eval[4]
        f1[measure][position]=eval[5]

measuresT=[]
for measureorder in measures:
        measure=measureorder[0]
        measuresT.append(measure)

cadena="Top"+"\t"+"\t".join(measuresT)
print(cadena)
sortida.write(cadena+"\n")

print("PRECISION:")

for position in [10,50,100,200,500,1000,2000]:
    values=[]
    for measureorder in measures:
        measure=measureorder[0]
        values.append(str(round(precision[measure][position],2)))
    cadena=str(round(total["raw_freq"][position]))+" & "+" & ".join(values)+"\\\\"
    print(cadena)
    sortida.write(cadena+"\n")
    sortida.write("\\hline\n")    
    
    
print("F1")
 
for position in [10,50,100,200,500,1000,2000]:
    values=[]
    for measureorder in measures:
        measure=measureorder[0]
        values.append(str(round(f1[measure][position],2)))
    cadena=str(round(total["raw_freq"][position]))+" & "+" & ".join(values)+"\\\\"
    print(cadena)
    sortida.write(cadena+"\n")
    sortida.write("\\hline\n")    