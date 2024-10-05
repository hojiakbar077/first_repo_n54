import threading
import time


def prime_nums(dest, start, stop):
    prime = bool
    for num in range(start, stop + 1):
        for d in range(2, num // 2 + 1):
            if num % d == 0:
                prime = False
                break
            else:
                prime = True

        if prime:
            dest.append(num)

    return dest


set_1 = []
set_2 = []
set_3 = []
set_4 = []


n = 100_000


t1 = threading.Thread(target=prime_nums, args=(set_1, 1, n // 4))
t2 = threading.Thread(target=prime_nums, args=(set_2, n // 4, n // 2))
t3 = threading.Thread(target=prime_nums, args=(set_3, n // 2, n // 4 * 3))
t4 = threading.Thread(target=prime_nums, args=(set_4, n // 4 * 3, n))

threads = [t1, t2, t3, t4]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


result = set_1 + set_2 + set_3 + set_4
end = time.time()

t = end - start
print(result)
print(t)
