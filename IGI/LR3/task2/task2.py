"""Task 2"""

from utils.addDescription import addDescription
from .loop import loop

@addDescription("Задание 2. Вычислить количество\
отрицательных чисел в заданной последовательности.\
Окончание ввода, новая строка или число большее 100.")
def task2():
    print("Вводите числа через пробел:")
    print(f"Результат. Количество отрицательных чисел: {loop()}")