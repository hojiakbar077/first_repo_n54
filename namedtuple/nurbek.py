from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'sound'])
animal1 = Animal('Lion', 'roar')
animal2 = Animal('cat', 'meow')
print(animal1)
print(animal2)
