import time


def time_check(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function has been performed for {run_time:.6f} seconds")
        return value
    return wrapper


@time_check
def exponentiation(numbers_list, y=2):
    return [x**y for x in numbers_list]


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
        for x in numbers_list:
            if x > 1:
                for i in range(2, x):
                    if x % i == 0:
                        break
                else:
                    res.append(x)
        return res


if __name__ == '__main__':
    print(exponentiation([1, 4, 5, 5, 7, 32]))
    print(get_filtred_numbers([1, 4, 5, 5, 7, 32], operation='prime'))

