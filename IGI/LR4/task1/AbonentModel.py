class AbonentModel:
    '''Data model of abonent.'''
    def __init__(self, name:str, num:str):
        self.name = name
        self.num = num

    def __str__(self) -> str:
        return self.name + ' ' + self.num

    def __eq__(self, value: object) -> bool:
        return value.name == self.name