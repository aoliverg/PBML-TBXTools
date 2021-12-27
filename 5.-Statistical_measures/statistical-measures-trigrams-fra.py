from TBXTools import *
from collections import defaultdict


total={}
correct={}
precision={}
recall={}
f1={}

extractor=TBXTools()
extractor.create_project("statistical1.sqlite","fra",overwrite=True)
extractor.load_sl_corpus("corpus-fra.txt")
extractor.loadSLTokenizer("MTUOC_tokenizer_fra")
extractor.ngram_calculation(nmin=3,nmax=3)
extractor.load_sl_stopwords("stop-fra.txt")
extractor.statistical_term_extraction()
extractor.save_term_candidates("candidates-stat-fra.txt")
extractor.load_evaluation_terms("corp_fr_terms_nes-trigrams.ann")

measures=[("raw_freq","desc"),("student_t","desc"),("chi_sq","asc"),("mi_like","desc"),("likelihood_ratio","asc"),("poisson_stirling","desc"),("pmi","asc"),("jaccard","desc")]
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

sortida=codecs.open("tables.txt","w",encoding="utf-8")

print("PRECISION:")
cadena="\\begin{table*}[ht]"
sortida.write(cadena+"\n")
cadena="\\begin{center}"
sortida.write(cadena+"\n")
cadena="\\begin{small}"
sortida.write(cadena+"\n")
cadena="\\begin{tabular}{|l|r|r|r|r|r|r|r|r|}"
sortida.write(cadena+"\n")
cadena="\\hline"
sortida.write(cadena+"\n")
cadena="\\rotatebox[origin=c]{90}{\\textbf{ Position }} & \rotatebox[origin=c]{90}{\\textbf{ raw\_freq }} & \rotatebox[origin=c]{90}{\\textbf{ student\_t }} & \rotatebox[origin=c]{90}{\\textbf{ chi\_sq }} & \rotatebox[origin=c]{90}{\\textbf{ mi\_like }} & \rotatebox[origin=c]{90}{\\textbf{ likelihood\_ratio }} &  \rotatebox[origin=c]{90}{\\textbf{ poisson\_stirling }} & \rotatebox[origin=c]{90}{\\textbf{ pmi }} & \rotatebox[origin=c]{90}{\\textbf{ jaccard }}\\\\"
sortida.write(cadena+"\n")
cadena="\\hline"
sortida.write(cadena+"\n")
for position in [10,50,100,200,500,1000,2000]:
    values=[]
    for measureorder in measures:
        measure=measureorder[0]
        values.append(str(round(precision[measure][position],2)))
    cadena=str(round(total["raw_freq"][position]))+" & "+" & ".join(values)+"\\\\"
    print(cadena)
    sortida.write(cadena+"\n")
    cadena="\\hline"
    sortida.write(cadena+"\n")  

   
cadena="\\end{tabular}"
sortida.write(cadena+"\n")
cadena="\\end{small}"
sortida.write(cadena+"\n")
cadena="\\end{center}"
sortida.write(cadena+"\n")
cadena="\\caption{\label{TABLEX} PRECISION DESCRIPTION.}"
sortida.write(cadena+"\n")
cadena="\\end{table*}"
sortida.write(cadena+"\n")

print("F1")

cadena="\\begin{table*}[ht]"
sortida.write(cadena+"\n")
cadena="\\begin{center}"
sortida.write(cadena+"\n")
cadena="\\begin{small}"
sortida.write(cadena+"\n")
cadena="\\begin{tabular}{|l|r|r|r|r|r|r|r|r|}"
sortida.write(cadena+"\n")
cadena="\\hline"
sortida.write(cadena+"\n")
cadena="\\rotatebox[origin=c]{90}{\\textbf{ Position }} & \rotatebox[origin=c]{90}{\\textbf{ raw\_freq }} & \rotatebox[origin=c]{90}{\\textbf{ student\_t }} & \rotatebox[origin=c]{90}{\\textbf{ chi\_sq }} & \rotatebox[origin=c]{90}{\\textbf{ mi\_like }} & \rotatebox[origin=c]{90}{\\textbf{ likelihood\_ratio }} &  \rotatebox[origin=c]{90}{\\textbf{ poisson\_stirling }} & \rotatebox[origin=c]{90}{\\textbf{ pmi }} & \rotatebox[origin=c]{90}{\\textbf{ jaccard }}\\\\"
sortida.write(cadena+"\n")
cadena="\\hline"
sortida.write(cadena+"\n")

for position in [10,50,100,200,500,1000,2000]:
    values=[]
    for measureorder in measures:
        measure=measureorder[0]
        values.append(str(round(f1[measure][position],2)))
    cadena=str(round(total["raw_freq"][position]))+" & "+" & ".join(values)+"\\\\"
    print(cadena)
    sortida.write(cadena+"\n")  
    cadena="\\hline"
    sortida.write(cadena+"\n")    
    
 
cadena="\\end{tabular}"
sortida.write(cadena+"\n")
cadena="\\end{small}"
sortida.write(cadena+"\n")
cadena="\\end{center}"
sortida.write(cadena+"\n")
cadena="\\caption{\label{TABLEX} F1 DESCRIPTION.}"
sortida.write(cadena+"\n")
cadena="\\end{table*}"
sortida.write(cadena+"\n")