from math import floor

runner_one = int(input())
runner_two = int(input())
runner_three = int(input())

total_time = runner_one + runner_two + runner_three
total_time_in_min = total_time // 60
total_time_in_sec = total_time % 60

total_time_in_min = floor(total_time_in_min)

if total_time_in_sec > 9:
    print(f'{total_time_in_min}:{total_time_in_sec}')
else:
    print(f'{total_time_in_min}:0{total_time_in_sec}')
