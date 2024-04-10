from .ISerializer import ISerializer
from .AbonentModel import AbonentModel
from .CSVSerializer import CSVSerializer
from .PickleSerializer import PickleSerializer
from .TelephoneBook import TelephoneBook

def task1():
    try:
        print("Task 1.")
        serializer: ISerializer
        filename: str
        lst = [AbonentModel("usr1", "12344"), AbonentModel("usr2", "9878"),
            AbonentModel("usr3", "123564")]
        print("Введите способ сериализации (1 - csv, 2 - pickle)")
        chs = input()
        if(chs == '1'):
           serializer = CSVSerializer
           filename = 'task1/task1.csv'
        elif(chs == '2'):
            serializer = PickleSerializer
            filename = 'task1/task1.pickle'
        else:
            raise ValueError
        
        tbook = TelephoneBook(serializer, filename)
        tbook.AddAbonents(lst)
        print("Abonents in the book")
        for i in lst:
            print('{} - {}'.format(i.name, i.num))
        print('Enter start string of the number you want to search:')
        sch = input()
        res = tbook.FindAbonentsByNum(sch)
        for i in res:
            print('{} - {}'.format(i.name, i.num))

    except ValueError as e:
        print("Value error!!! Try again...") 