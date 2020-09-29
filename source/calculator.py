def add(*args):
    return sum(args)


def sub(a, b):
    return a - b


def mul(*args):
    result = 1
    for i in args:
        result *= i
    if not result:
        raise(ValueError)
    return result


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return -float('inf') if a < 0 else float('inf')


def avg(iterable,
        lower_bound=-float('inf'),
        upper_bound=float('inf')):
    iterable = [i for i in iterable if lower_bound <= i <= upper_bound]
    return sum(iterable) / len(iterable)
