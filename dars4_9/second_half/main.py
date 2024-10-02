from threading import Thread

from requests import get


def request_getter():
    print(sum(range(1, 10**9)))


for i in range(10000):
    thread = Thread(target=request_getter)
    thread.start()