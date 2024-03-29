"""Function of start task 1."""

from utils.addDescription import addDescription
from .taylor import taylor

@addDescription("Задание 1. Написать программу для вычисления ряда Тейлора функции arcsin(x).")
def task1():
    try:
        print("Введите x:")
        x = float(input())
        print("Введите eps:")
        eps = float(input())
        n, F, mathF = taylor(x, eps)
        print("Результат.....")
        print(f"| x = {x} | n = {n} | F = {F} | mathF = {mathF} | eps = {eps} |")
    except ValueError as er:
        print("ValueError!!! Try again...")

