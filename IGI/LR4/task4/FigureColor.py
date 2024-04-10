
class FigureColor:
    '''Class of figure color.'''
    def __init__(self, color = "unknown"):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def set_color(self, newcolor:str):
        if(self.__color is not newcolor):
            self.__color = newcolor
