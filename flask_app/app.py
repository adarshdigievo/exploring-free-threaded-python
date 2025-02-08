import threading

from flask import Flask
import time

import tempfile
import os

from check_gil import show_gil_status

app = Flask(__name__)


# CPU-bound task
def heavy_computation():
    return sum(i * i for i in range(10 ** 7))


# Routes
@app.route('/cpu')
def cpu_bound():
    print(threading.active_count())
    heavy_computation()
    return "CPU task done!"


@app.route('/io')
def io_bound():
    print(threading.active_count())

    with tempfile.TemporaryFile() as f:
        f.write(b"Hello, World!" * 10000000)
        f.seek(0)
        f.read()
        f.write(b"Hi, World!" * 10000000)

        os.remove(f.name)  # Added for more IO work

    return "IO task done!"


if __name__ == '__main__':

    show_gil_status()

    app.run()
