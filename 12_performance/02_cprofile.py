import sys
import functools


@functools.lru_cache()
def fibonacci_cached(n):
    return n if n < 2 else fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = 30
    if sys.argv[-1] == 'cache':
        fibonacci_cached(n)
    else:
        fibonacci(n)

