import timeit

from check_gil import show_gil_status


def single_threaded_benchmark():
    show_gil_status()

    # Define the code to be timed
    code_to_test = """
    
total = 0
for i in range(1_000_000):
    total += i

"""

    # Use timeit to measure execution time
    execution_time = timeit.timeit(code_to_test, number=100)

    print(f"Execution time: {execution_time:.6f} seconds")


if __name__ == '__main__':
    single_threaded_benchmark()
