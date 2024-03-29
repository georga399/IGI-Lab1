"""Lab work #3.
Variant 2.
© by Azarov Egor
Entry point.

"""

from runTask import runTask

if __name__ == "__main__":
    print("Лабораторная работа №3.")
    print("Вариант 2.")
    print("© Азаров Е.А. гр.253505")
    while(True):   
        runTask()
        print("To continue press <enter>. To exit write: n (N):")    
        chs = input()
        if(chs == 'n' or chs == 'N'):
            print("Good luck!")
            break