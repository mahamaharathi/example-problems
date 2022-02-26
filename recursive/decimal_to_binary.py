def decimal_to_binary(num):
    assert int(num) == num, 'The parameter must be integer'
    if num / 2 == 0:
        return str(num % 2)
    return str(decimal_to_binary(int(num/2))) + str(num % 2)


print(decimal_to_binary(10))


def dec_to_binary(num):
    assert int(num) == num, 'The parameter must be integer'
    if num == 0:
        return 0
    return num % 2 + 10 * dec_to_binary(int(num/2))


print(dec_to_binary(10))
