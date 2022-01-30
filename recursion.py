"""
recursion fibonacci and factorial examples



no changes to be done sorry


"""

def fibonacci_recursive(n):
    if n<2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    curr = 1
    prev = 1
    for _ in range(n - 1):
        curr, prev = curr + prev, curr
    return curr


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    return result
