from collections import namedtuple

Car = namedtuple("Cars", ["nomi", "hazili"])

car = Car("GM", "BAycot")

print(car.nomi, car.hazili)

