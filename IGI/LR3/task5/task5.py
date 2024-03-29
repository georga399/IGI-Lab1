"""Task 5."""

from utils.addDescription import addDescription
from .findOddMult import findOddMult
from .findCustomSum import findCustomSum

@addDescription("Задание 5. Найти произведение элементов с чётными номерами \
и сумму элементов, расположенных между первым и последним нулевым элементом")
def task5():
    print("Вводите вещественные элементы через пробел (окончание ввода <enter>):")
    text = input()
    lst = []
    for p in text.split(' '):
        try:
            el = float(p)
            lst.append(el)
        except ValueError as er:
            print("Wrong value!!! Try again...")
            return
    print("Вы ввели следующий список:")
    print(lst)
    print("Произведение элементов с нечетными номерами")
    print(findOddMult(lst))
    print("Сумма элементов, расположенных между первым и последним нулевым элементом:")
    print(findCustomSum(lst))