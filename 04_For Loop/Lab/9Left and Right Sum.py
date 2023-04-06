n = int(input())
sum_left = 0
sum_right = 0

for number_left in range(1, n + 1):
    left_n = int(input())
    sum_left += left_n

for number_right in range(1, n + 1):
    right_n = int(input())
    sum_right += right_n

if sum_left == sum_right:
    print(f'Yes, sum = {sum_left}')
elif sum_left >= sum_right or sum_left <= sum_right:
    difference_sum = abs(sum_left - sum_right)
    print(f'No, diff = {difference_sum}')
