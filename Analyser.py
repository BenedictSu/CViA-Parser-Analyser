from sets import Set
from Parser import Parser, PDFConverter, Tokenizer

class Analyser:
    pLang = Set(["c++", "objective c", "c#", "java", "swift", "python", "cobol",
                     "haskell", "javaSctipt", "latex", "matlab", "objective-c", "pascal",
                     "php", "prolog", "ruby", "scheme", "tex", "unity", "unix shell"])
    sLang = Set(["english", "mandarin", "chinese", "indonesian", "tamil", "malay",
                 "japanese", "malay", "russian", "french"])
    global fields
    fields = [pLang, sLang]
    
    def __init__(self, jdTokens, cvTokens):
        self.jdTokens = jdTokens
        self.cvTokens = cvTokens

    def countIntScore (self):
        score = [0, 0]

        jd = Parser(self.jdTokens)
        cv = Parser(self.cvTokens)
        
        count = 0
        for field in fields:
            jdMat = jd.match(field)
            cvMat = cv.match(field)
            score[count] = self.countMatches(jdMat, cvMat) 
            count += 1
        return score
    
    def countMatches (self, categories, template):
        total = 0
        matched = 0
        for cat in categories:
            if cat in template:
                matched += 1
            total += 1
        if total != 0:
            return float(matched) / total
        else:
            return 0;
