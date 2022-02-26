def power_of_numbers(number, power):
    assert power >= 0 and int(
        power) == power, 'Power should be greater than or equal to Zero'
    if power == 0:
        return 1

    return number * power_of_numbers(number, power - 1)


print(power_of_numbers(-5, 3))
