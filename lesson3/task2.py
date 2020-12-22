from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'-->{func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'<--{func.__name__}({signature}) == {value}')
        return value
    return wrapper


@trace
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    fib(3)
