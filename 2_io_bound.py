import os
import tempfile
import time
import threading
from concurrent.futures import ThreadPoolExecutor

from check_gil import show_gil_status


def io_bound():
    with tempfile.TemporaryFile() as f:
        f.write(b"Hello, World!" * 10000000)
        f.seek(0)
        f.read()
        f.write(b"Hi, World!" * 10000000)

        os.remove(f.name)  # Added for more IO work

    return "IO task done!"


# Single-threaded
def single_threaded():
    io_bound()


# Multi-threaded
def multi_threaded():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(io_bound)


def run_benchmark():
    # Timing
    start = time.time()
    for _ in range(10):
        single_threaded()
        # the io_bound() is called 10 times

    print(f"Single thread Exec Time: {time.time() - start:.2f}s")

    start = time.time()
    for _ in range(4):
        multi_threaded()
        # the io_bound() is called 20 times
    print(f"Multi thread Exec Time: {time.time() - start:.2f}s")


if __name__ == '__main__':
    show_gil_status()

    run_benchmark()
