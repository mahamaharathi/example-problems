from numpy import array


list_a = [5, 2, -1, 6, -2, 7, 3]

k = 3
# length_of_array = len(list_a)
# sliding_index = 0
# max_sum = list_a[0] + list_a[1] + list_a[2]
# while sliding_index + 2 < length_of_array - 1:
#     calculated_sum = list_a[sliding_index] + \
#         list_a[sliding_index+1] + list_a[sliding_index+2]
#     if calculated_sum > max_sum:
#         max_sum = calculated_sum
#         print("a")

# print(max_sum)


def max_sum(array, k):
    max_sum = 0
    current_sum = 0
    for i in range(k):
        current_sum = current_sum + array[i]
        max_sum = current_sum
    for i in range(k, len(array)):
        current_sum = current_sum - array[i-k] + array[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


a = max_sum(list_a, 3)
print(a)
