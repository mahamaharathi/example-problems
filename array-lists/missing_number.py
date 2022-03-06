# find the missing number in array of 1 to 100

list_of_numbers = list(range(1, 101))

# Assume missing number is 56
list_of_numbers.remove(56)


def missing_number(array):
    sum1 = 100 * 101 / 2
    sum2 = sum(array)
    print(f'missing number = {sum1 - sum2}')


missing_number(list_of_numbers)