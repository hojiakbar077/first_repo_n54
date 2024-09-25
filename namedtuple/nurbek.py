from collections import namedtuple

Animal = namedtuple("Animal", ["type", "sound"])

crocodile = Animal("crocodile", "ggggggg")

print(crocodile.type, crocodile.sound)
