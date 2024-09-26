from collections import namedtuple

Animal = namedtuple("Animal", ["type", "sound"])

dog = Animal("dog", "gaff")

print(dog.type, dog.sound)
