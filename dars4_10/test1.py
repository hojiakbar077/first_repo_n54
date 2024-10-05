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


result = []

start = time.time()
prime_nums(result, 1, 100_000)
end = time.time()

t = end - start

print(result)
print(t)
