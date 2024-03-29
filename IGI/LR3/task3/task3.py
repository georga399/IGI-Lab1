"""Task 3"""
from utils.addDescription import addDescription
from task3.isBinary import isBinary

@addDescription("Задание 3. Определить,\
является ли введенная с клавиатуры строка двоичным числом.")
def task3():
    print("Введите строку:")
    if isBinary():
        print("Данная строка является двоичным числом.")
    else:
        print("Данная строка НЕ является двоичным числом.")