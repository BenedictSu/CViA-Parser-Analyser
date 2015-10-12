# for PDFConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

# for Tokenizer
import nltk, re, pprint, sets

from nltk.corpus import treebank_chunk

# reference to http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
class PDFConverter:
    def __init__(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
            password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        self.str = retstr.getvalue()
        retstr.close()

# reference to http://www.nltk.org/book/ch07.html
class Tokenizer
    def __init__ (self, cFile):
        tokens = nltk.wordpunct_tokenize(cFile)
        self.tokens = sets.Set(tokens)

pdfFilePath = raw_input("Please enter the location of the JD in pdf format: ")
jd = PDFConverter(pdfFilePath)
jd = jd.str.decode('utf-8')
pdfFilePath = raw_input("Please enter the location of the CV in pdf format: ")
cv = PDFConverter(pdfFilePath)
cv = cv.str.decode('utf-8')

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
