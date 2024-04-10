class NameableMixin:
    '''Mixin class with method getName().'''
    def __init__(self, name) -> None:
        self.__name = name
    def getName(self):
        return self.__name