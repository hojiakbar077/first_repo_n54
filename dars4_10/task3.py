from threading import Thread, Lock

import time

counter = 0


def race(num):
    global counter

    lock.acquire()

    for i in range(num):
        counter += 1
        
    lock.release()


lock = Lock()

start = time.time()
t1 = Thread(target=race, args=(50_000_000, ))
t2 = Thread(target=race, args=(50_000_000, ))
stop = time.time()

time = stop - start

print(time)
