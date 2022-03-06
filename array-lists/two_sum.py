# given a list of numbers find the pairs that return a given sum

list_of_numbers = [1, 2, 3, 4, 5, 6]

target_sum = 9

list_of_pairs = []


def two_sum(arr, target_sum):

    for i in range(len(list_of_numbers)):
        first_number = arr[i]
        required_second_number = target_sum - first_number
        if required_second_number in list_of_numbers and first_number != required_second_number:
            list_of_pairs.append(tuple(sorted([first_number, required_second_number])))


two_sum(list_of_numbers, target_sum)
print(set(list_of_pairs))