n = int(input())
sum_even = 0
sum_odd = 0

for number in range(1, n + 1):
    value = int(input())
    if number % 2 == 0:
        sum_even += value
    else:
        sum_odd += value
if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_odd}')
else:
    diff_sum = abs(sum_even - sum_odd)
    print('No')
    print(f'Diff = {diff_sum}')
