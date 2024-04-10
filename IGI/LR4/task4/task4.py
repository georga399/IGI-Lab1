from .FigureColor import FigureColor
from .GeometricFigure import GeometricFigure
from .Romb import Romb

def task4():
    try:
        print("Input a diagonals of Romb:")
        a = float(input())
        print("Input b diagonals of Romb:")
        b = float(input())
        if(a <= 0 or b <= 0):
            raise ValueError
        print("Input color name:")
        color = input()
        romb = Romb(a,b,color)
        print(romb)
        with open('task4/task4.txt', 'w') as f:
            f.write(str(romb))
    except ValueError as e:
        print("Value error!!! Try again...")