# reference to http://www.nltk.org/book/ch07.html
import nltk, re, pprint

from Parser import convert_pdf_to_file

pdfFilePath = raw_input("Please enter the location of the CV in pdf format: ")

convertedFile = convert_pdf_to_file(pdfFilePath).decode('utf-8')

def processing (cFile):
    tokens = nltk.word_tokenize(cFile)

    taggedTokens = nltk.pos_tag(tokens)

    chunked = nltk.chunk.ne_chunk(taggedTokens, False)

    print chunked

processing(convertedFile)
