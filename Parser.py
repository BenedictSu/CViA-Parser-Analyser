# for PDFConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

# for Tokenizer
import nltk, re, pprint, sets

from nltk.corpus import treebank_chunk

# for Parser
from sets import Set

# reference to http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
class PDFConverter:
    def __init__(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = "utf-8"
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, "rb")
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
        self.str = retstr.getvalue().decode("utf-8")
        retstr.close()

# reference to http://www.nltk.org/book/ch07.html
class Tokenizer:
    def __init__ (self, cFile):
        tokens = nltk.wordpunct_tokenize(cFile)
        self.tokens = Set()
        for token in tokens:
            self.tokens.add(token.lower())

class Parser:
    def __init__ (self, text):
        self.tokens = text

    def match (self, categories):
        matches = Set()
        for cat in categories:
            if cat in self.tokens:
                matches.add(cat)
        return matches
