import time
from concurrent.futures import ThreadPoolExecutor

from check_gil import show_gil_status

EXECUTION_COUNT = 50


def calculate():
    # calculate squares of numbers till 10^7
    return sum(i * i for i in range(10 ** 6))


def multi_threaded():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(EXECUTION_COUNT):
            executor.submit(calculate)


def run():
    show_gil_status()

    # Single-threaded
    start = time.time()
    for _ in range(EXECUTION_COUNT):
        calculate()
    print(f"Single thread Exec Time: {time.time() - start:.2f}s")

    # Multi-threaded
    start_2 = time.time()
    multi_threaded()
    print(f"Multi thread Exec Time: {time.time() - start_2:.2f}s")


if __name__ == '__main__':
    run()
