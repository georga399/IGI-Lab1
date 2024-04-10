from .ISerializer import ISerializer
from .AbonentModel import AbonentModel

class TelephoneBook:
    '''Model of telephone book.'''
    def __init__(self, serialializer:ISerializer, filename:str):
        self.__serializer = serialializer
        self.__filename = filename
    
    def AddAbonents(self, abonents:list):
        allAbons = self.__serializer.DeserializeFromFile(self.__filename)
        allAbons.extend(abonents)
        self.__serializer.SerializeToFile(allAbons, self.__filename)

    def FindAbonentsByNum(self, numst:str):
        allAbons = self.__serializer.DeserializeFromFile(self.__filename)
        matchedAbons = []
        for ab in allAbons:
            num:str = ab.num
            if(num.startswith(numst)):
                matchedAbons.append(ab)
        return matchedAbons

    
    