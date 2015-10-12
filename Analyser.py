# reference to http://www.nltk.org/book/ch07.html
import nltk, re, pprint, sets

from Parser import convert_pdf_to_file
from nltk.corpus import treebank_chunk

pdfFilePath = raw_input("Please enter the location of the JD in pdf format: ")
jd = convert_pdf_to_file(pdfFilePath).decode('utf-8')
pdfFilePath = raw_input("Please enter the location of the CV in pdf format: ")
cv = convert_pdf_to_file(pdfFilePath).decode('utf-8')

def processing (cFile):
    tokens = nltk.wordpunct_tokenize(cFile)
    tset = sets.Set(tokens)
    return tset
    
cv = processing(cv)
jd = processing(jd)

total = 0
matched = 0
for key in cv:
    if key in jd:
        matched += 1
    total += 1

print "The percentage matched is: "
print float(matched) / total
