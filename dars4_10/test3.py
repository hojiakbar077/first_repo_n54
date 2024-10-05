import time

counter = 0


def race(num):
    global counter

    for i in range(num):
        counter += 1


start = time.time()

race(100_000_000)

stop = time.time()

time = stop - start

print(time)
