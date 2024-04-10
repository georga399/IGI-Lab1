import abc
import pickle

class ISerializer:
    '''Abstract class of serializer.'''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def SerializeToFile(objs:list, filename:str):
        pass

    @abc.abstractmethod
    def DeserializeFromFile(filename:str) -> list:
        pass

        