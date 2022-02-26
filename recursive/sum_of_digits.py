def sum_of_digits(digits):
    assert digits >= 0 and int(
        digits) == digits, 'Number must be positive integer'
    if digits == 0:
        return 0
    return sum_of_digits(int(digits/10)) + digits % 10


print(sum_of_digits(1))
