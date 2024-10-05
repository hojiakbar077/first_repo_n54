import multiprocessing
import time

file = "big.txt"
file2 = "big2.txt"


def read_file(filepath):
    with open(filepath) as file:
        content = file.read()

    length = 0
    for word in content:
        length += 1

    return length


if __name__ == "__main__":
    start = time.time()
    with multiprocessing.Pool(processes=8) as pool:
        result = pool.map(read_file, (file, file2))
    end = time.time()

    time = end - start
    print(result)
    print(time)
