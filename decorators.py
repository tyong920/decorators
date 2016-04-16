#! /usr/bin/env python
import time
import functools


def greeting_before_and_after_call(greeting):
    """
    A decorator to greeting.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Hi {}'.format(greeting))
            res = func(*args, **kwargs)
            print('Bye Bye {}'.format(greeting))
            return res
        return wrapper
    return decorator


def benchmark(func):
    """
    A decorator to time the activity of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('{} runs {}s'.format(func.__name__, end-start))
        return res
    return wrapper


@benchmark
@greeting_before_and_after_call('Tyong')
def print_reversed_string(a_string):
    for __ in reversed(a_string):
        print(__)


if __name__ == '__main__':
    print_reversed_string('Import this')
