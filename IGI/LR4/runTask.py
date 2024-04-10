from task1.task1 import task1
from task2.task2 import task2  
from task3.task3 import task3
from task4.task4 import task4
from task5.task5 import task5

def runTask():
    """Run selected task of lab work."""
    print("Укажите номер задания(1-5):")
    try:
        chs = int(input())
        match chs:
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task5()
            case _:
                print("Undefined task!!! Try again...")
    except ValueError as er:
        print("Wrong parameter!!! Try again...")
    except EOFError as er:
        print("EOFError!!! Try again...")