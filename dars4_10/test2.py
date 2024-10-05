import time


def read_file(filepath):
    with open(filepath) as file:
        content = file.read()

    length = 0
    for word in content:
        length += 1

    return length


start = time.time()
print(read_file("big.txt"))
print(read_file("big2.txt"))
end = time.time()

time = end - start

print(time)
