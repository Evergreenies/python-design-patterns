# Filename      :       decorator_function.py
# Created By    :       Suyog Shimpi
# Created Date  :       24/05/22
import time


def time_it(func):
    def wrapper():
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f'{func.__name__} took {int((end - start) * 1000)}ms')
        return result

    return wrapper


@time_it
def some_op():
    print('starting operation...')
    time.sleep(1)
    print('We are done')
    return 123


if __name__ == '__main__':
    print(some_op())
