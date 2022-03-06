days_of_temp = int(input("How many days temperature"))
count = 0

list_of_temps = []
while count < days_of_temp:
    input_temp = int(input("Enter highest temperature"))
    list_of_temps.append(input_temp)
    count += 1

avg = sum(list_of_temps) / len(list_of_temps)

days_above_avg = 0
for i in list_of_temps:
    if i > avg:
        days_above_avg += 1
print(f'avg temp: {sum(list_of_temps)/ len(list_of_temps)}')
print(f'{days_above_avg} are above average temp')