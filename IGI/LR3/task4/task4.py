"""Task 4"""
from utils.addDescription import addDescription
from .countOfLowers import countOfLowers
from .removeStartWirhS import removeStartWithS
from .findFirstVWord import findFirstVWord

@addDescription("Задание 4. a)Определить количество строчных букв в строке;\n\
б) найти первое слово, содержащее букву 'v' и его номер;\n\
в) вывести строку, исключив из нее слова, начинающиеся с 's'.")
def task4():
    print("Ввведите строку:")
    text = input()
    print(f"Количество строчных букв:{countOfLowers(text)}")
    pos, word = findFirstVWord(text)
    if(pos == -1):
        print("Слово, содержащее v не найдено")
    else:
        print(f"Позиция первого слова, содержащее v: {pos}, слово:{word}")
    print("Текст после удаления слов, начинающиюхся с буквой s:")
    print(removeStartWithS(text))