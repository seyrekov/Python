hours = int(input())
minutes = int(input())
hours_in_minutes = hours * 60
time = hours_in_minutes + minutes
actual_time = time + 15
final_time_hours = actual_time // 60
final_time_minutes = actual_time % 60

if final_time_hours == 24:  # we transform 24.14 into 0.14
    final_time_hours = 0

if 0 <= final_time_minutes <= 9:
    print(f'{final_time_hours}:0{final_time_minutes}')
elif 9 < final_time_minutes <= 59:
    print(f'{final_time_hours}:{final_time_minutes}')
