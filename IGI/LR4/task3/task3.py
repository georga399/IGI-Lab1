import numpy as np
from .taylor import taylor
from .graph import graph

def task3():
    try:
        print("Вычисление по тейлору asin(x)")
        print("Введите x:")
        x = float(input())
        print("Введите n:")
        n = int(input())
        F, eps, mathF, mean, median, mode, variance, std = taylor(x, n)
        print("Результат.....")
        print(f"| x = {x} | n = {n} | F = {F} | mathF = {mathF} | eps = {eps} |")
        print(f"mean: {mean}")
        print(f"median: {median}")
        print(f"mode: {mode}")
        print(f"variance: {variance}")
        print(f"std: {std}")
        x = np.arange(-1, 1, 0.1)
        y1 = []
        y2 = []
        for i in x:
            F1, eps1, mathF1, _, _, _, _, _ = taylor(float(i), n)
            y1.append(mathF1)
            y2.append(F1) 
        graph(x, y1, x, y2)

    except ValueError as er:
        print(f"ValueError!!! Try again...")

