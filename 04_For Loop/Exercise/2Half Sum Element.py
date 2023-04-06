import sys
n = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for number in range(n):  # we could use instead (0, n) because it is equal to our aim
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number
if max_number == sum_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(max_number - (sum_numbers - max_number))
    print('No')
    print(f'Diff = {difference}')
