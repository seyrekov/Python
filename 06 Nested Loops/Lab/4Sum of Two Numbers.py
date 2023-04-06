start_range = int(input())
finish_range = int(input())
number_magic = int(input())
combination_number = 0
number_founded = False
combinations = 0
pass_rate = 0


for x in range(start_range, finish_range + 1):
    for y in range(start_range, finish_range + 1):
        combination_number += 1
        if x + y == number_magic:
            print(
                f'Combination N:{combination_number} ({x} + {y} = {number_magic})')
            number_founded = True
            pass_rate = 1
            break
        else:
            combinations += 1
    if number_founded:
        break

if pass_rate == 0:
    print(f'{combinations} combinations - neither equals {number_magic}')
