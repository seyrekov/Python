name = input()
repeat = 0
sum_evaluation = 0
level_class = 1
excluded = False

while level_class <= 12:
    evaluation = float(input())
    if evaluation < 4:
        repeat += 1
        if repeat > 1:
            excluded = True
            break
        continue
    sum_evaluation += evaluation
    level_class += 1

if excluded:
    print(f'{name} has been excluded at {level_class} grade')
else:
    average_evaluation = sum_evaluation / 12
    print(f'{name} graduated. Average grade: {average_evaluation:.2f}')
