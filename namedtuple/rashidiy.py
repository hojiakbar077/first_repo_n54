from collections import namedtuple

Animal = namedtuple('Animal', 'name sound')
cat = Animal('cat', 'meow')
print(cat.sound)