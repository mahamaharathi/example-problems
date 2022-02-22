list_a = [10, 20, 35, 50, 75, 80, 85]
sum = 70

# kinda brute force method
# for i in list_a:
#     if (sum - i) in list_a:
#         print(i, sum - i)
length_of_array = len(list_a)

left_index = 0
right_index = length_of_array - 1
while left_index < right_index:
    if list_a[left_index] + list_a[right_index] == sum:
        print(list_a[left_index], list_a[right_index])
        break
    elif list_a[left_index] + list_a[right_index] < sum:
        left_index += 1
    elif list_a[left_index] + list_a[right_index] > sum:
        right_index -= 1


# Two pointer method
