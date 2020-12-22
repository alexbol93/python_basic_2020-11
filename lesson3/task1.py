import time
from functools import wraps
from operator import pow


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function {func.__name__} has been performed for {run_time:.6f} seconds")
        return value
    return wrapper


@time_check
def exponentiation(numbers_list, y=2):
    return list(map(pow, numbers_list, [y for elem in range(len(numbers_list))])) #Не знаю как передать у=2 вторым аргументом в pow, пришлось генерить список из у, list comprehension выглядит проще здесь


@time_check
def get_filtred_numbers(numbers_list, operation='even'):
    res = []
    if operation not in ['even', 'odd', 'prime']:
        print(f'Укажите корректное название операции even, odd, prime')
    if operation == 'even':
        return [x for x in numbers_list if x % 2 == 0]
    elif operation == 'odd':
        return [x for x in numbers_list if x % 2 != 0]
    elif operation == 'prime':
        return [x for x in numbers_list if is_prime_number(x)]


def is_prime_number(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print(exponentiation([1, 4, 5, 5, 7, 32]))
    print(get_filtred_numbers([1, 2, 4, 5, 5, 7, 32], operation='prime'))

