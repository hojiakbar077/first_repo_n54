from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'voice'])

animal = Animal(name='Cat',voice='meow')

print(animal.name)  
print(animal.voice)  
