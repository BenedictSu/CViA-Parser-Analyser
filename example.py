from Parser import PDFConverter, Tokenizer
from Analyser import Analyser, Calculator


pdfFilePath = raw_input("Please enter the location of the JD in pdf format: ")
jd = PDFConverter(pdfFilePath).str
pdfFilePath = raw_input("Please enter the location of the CV in pdf format: ")
cv = PDFConverter(pdfFilePath).str

jd = Tokenizer(jd).tokens
cv = Tokenizer(cv).tokens

jd = Analyser(jd, cv)
jd = jd.countIntScore()

jd = Calculator(jd)

print "The score is: "
print jd.countScore()
