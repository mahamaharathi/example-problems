def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    ans = fibonacci(n-1) + fibonacci(n-2)
    return ans


print(fibonacci(15))
