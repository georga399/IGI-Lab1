from .GeometricFigure import GeometricFigure
from .FigureColor import FigureColor
from .NameableMixin import NameableMixin

class Romb(NameableMixin, GeometricFigure):
    '''Realization of romb.'''
    def __init__(self, a:float, b:float, color:str) -> None:
        self.__a = a
        self.__b = b
        self.__color = FigureColor(color)
        super().__init__('Romb')

    def calculateS(self):
        return self.__a * self.__b

    def __str__(self) -> str:
        S = self.calculateS()
        super().calculateS()
        figure = '''\
                 /\\
                /##\\
               /####\\
              /######\\
             /########\\
            /##########\\
           /############\\
          /##############\\
         /################\\
        <##################>
         \\################/
          \\##############/
           \\############/
            \\##########/
             \\########/
              \\######/
               \\####/
                \\##/
                 \\/
'''  
        return '{}\nFigure: {}. a = {}, b = {}. S = {}. Color = {}.'.format(
            figure,
            self.getName(),
            self.__a, self.__b, S, self.__color.color
        )