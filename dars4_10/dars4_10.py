import multiprocessing as mp
import time


def calculate_sum(numbers):
    return sum(numbers)


if __name__ == '__main__':
    ps = mp.Pool(processes=500)

    numbers = range(500_000_000)

    start = time.time()
    results = ps.map(calculate_sum, [numbers for _ in range(50)])
    ps.close()
    ps.join()
    end = time.time()
    print(results)
    print("Multiprocessing with Pool:", end - start)

    # Single-threaded approach
    # start = time.time()
    # results_single = [calculate_sum(numbers) for _ in range(10)]
    # end = time.time()

    # print("Single Process:", end - start)
    # print(results_single)
