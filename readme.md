# Goodbye GIL: Exploring the Free-threaded mode in Python 3.13

[Slides: Goodbye GIL_ Exploring the Free-threaded mode in Python 3.13.pdf](Slides%20-%20Goodbye%20GIL_%20Exploring%20the%20Free-threaded%20mode%20in%20Python%203.13.pdf)

## Running Code Examples

- Create two separate venvs - One with free-threaded interpreter and the other with the default interpreter.
- Run each code snippet with both of these to benchmark execution
- Instructions for free-threaded setup: [link](https://py-free-threading.github.io/installing_cpython/)

## Flask app

- Install requirements (flask library).
- Run app.py and run the benchmark scripts using k6.
- Benchmarking tool used is k6: [download from here](https://k6.io/open-source/). Run as `k6 run <benchmark_file_name>`


