sum_simple_numbers = 0
sum_complicated_numbers = 0
command = input()
while command != 'stop':
    is_simple = True
    cur_num = int(command)
    if cur_num < 0:
        print('Number is negative.')
        command = input()
        continue
    for digit in range(2, cur_num):
        if cur_num % digit == 0:
            is_simple = False
            break
    if is_simple:
        sum_simple_numbers += cur_num
    else:
        sum_complicated_numbers += cur_num
    command = input()
print(f"Sum of all prime numbers is: {sum_simple_numbers}")
print(f"Sum of all non prime numbers is: {sum_complicated_numbers}")
