def factorial(n):
    assert n >= 0 and int(n) == n, 'Number must be positive integer'
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
