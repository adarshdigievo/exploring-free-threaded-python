import sys
import sysconfig


def show_gil_status():
    gil_status = sys._is_gil_enabled()
    print(F"{sys._is_gil_enabled()=}")

    if gil_status:
        print("Running in default interpreter - GIL is enabled")
    else:
        print("Running in Free threaded interpreter - GIL is disabled")

def check_free_threading_support():
    print(f"{sysconfig.get_config_vars().get('Py_GIL_DISABLED')=}")


if __name__ == '__main__':
    check_free_threading_support()

    show_gil_status()

