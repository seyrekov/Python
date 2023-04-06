hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())
time_exam = hour_exam * 60 + minute_exam
time_arrival = hour_arrival * 60 + minute_arrival

if time_exam < time_arrival:
    print('Late')
elif time_exam - 30 <= time_arrival <= time_exam:
    print('On time')
elif time_exam > time_arrival:
    print('Early')
if time_exam - 60 < time_arrival < time_exam:
    mm = time_exam - time_arrival
    print(f'{mm} minutes before the start')
elif time_arrival <= time_exam - 60:
    timing = time_exam - time_arrival
    hh = timing // 60
    mm = timing % 60
    # this if could be replaced with - > print(f'{hh}:{mm:0>2d} hours before the start')
    if mm < 10:
        print(f'{hh}:0{mm} hours before the start')
    else:
        print(f'{hh}:{mm} hours before the start')
elif time_exam < time_arrival < time_exam + 60:
    timing = time_arrival - time_exam
    print(f'{timing} minutes after the start')
elif time_exam + 60 <= time_arrival:
    timing = time_arrival - time_exam
    hh = timing // 60
    mm = timing % 60
    if mm < 10:
        print(f'{hh}:0{mm} hours after the start')
    else:
        print(f'{hh}:{mm} hours after the start')
