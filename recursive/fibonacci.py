def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Number must be positive integer'
    if n == 1 or n == 0:
        return n

    ans = fibonacci(n-1) + fibonacci(n-2)
    return ans


print(fibonacci(7))
