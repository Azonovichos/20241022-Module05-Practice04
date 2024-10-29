# Module 5 Practice 4

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        new_house = super().__new__(cls)
        cls.houses_history.append(args[0])
        return new_house

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

'''class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        self_ = (first, second, third)
        print(self_)
        print(id(self_))
        self = (first, second, third)
        print(self)
        print(id(self))
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)'''