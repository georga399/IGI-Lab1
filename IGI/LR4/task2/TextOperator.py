import re

from numpy import sort

class TextOperator:
    '''Class for operating with text.'''
    def __init__(self, text = '') -> None:
        self.__text = text
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, input_text):
        self.__text = input_text
    
    def sentencesCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        return len(sentences)

    def declSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[.]', self.__text)
        return len(sentences)

    def exclSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!]', self.__text)
        return len(sentences)

    def interrogSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[?]', self.__text)
        return len(sentences)

    def medSentSize(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        sizesum = 0
        for snt in sentences:
            snt = snt.replace(',', '').replace(';', '')
            sizesum += len(snt.split())
        return sizesum/len(sentences)

    def medWordSize(self):
        text = self.__text.replace(',', '')\
            .replace(';', '').replace('.', '')\
            .replace('!', '').replace('?', '').replace('\n', '')
        wordCounter = 0
        sizeSum = 0
        for w in text.split():
            if(w == ''):
                continue
            wordCounter+=1
            sizeSum+=len(w)

    def emojisCount(self):
        emojis = re.findall(r'[:;][-]*([[]+|[(])', self.__text)
        return len(emojis)
    
    def wordsCount(self):
        text = self.__text.replace(',', '')\
            .replace(';', '').replace('.', '')\
            .replace('!', '').replace('?', '').replace('\n', '')
        wordCounter = 0
        for w in text.split():
            if(w == ''):
                continue
            wordCounter+=1
        return wordCounter

    def getWordsList(self):
        text = self.__text.replace(',', '')\
            .replace(';', '').replace('.', '')\
            .replace('!', '').replace('?', '').replace('\n', '')
        lst = []
        for w in text.split():
            if(w == ''):
                continue
            lst.append(w)
        return lst

    def findCapit(self):
        pattern = re.compile('[a-z][A-Z]', re.S)
        text = pattern.sub(lambda m: '_' + m.group() + '_', self.__text)
        return text
    
    def wordsCountLess7(self):
        text = self.__text.replace(',', '')\
            .replace(';', '').replace('.', '')\
            .replace('!', '').replace('?', '').replace('\n', '')
        return sum(1 for w in text.split() if len(w) < 7)

    def findSmallestWordEndsWithA(self):
        text = self.__text.replace(',', '')\
            .replace(';', '').replace('.', '')\
            .replace('!', '').replace('?', '').replace('\n', '')
        aword = ''
        awordSize = 1e9
        for w in text.split():
            if w.endswith('a') and len(w) < awordSize:
                aword = w
                awordSize = len(aword)
        return aword

    def sortWordsInDesc(self):
        lst = self.getWordsList()
        lst = sorted(lst, key=lambda x: len(x), reverse=True)
        return lst
