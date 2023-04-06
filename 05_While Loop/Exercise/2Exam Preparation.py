eligible_number_fails = int(input())
order = 'Enough'
number_fails = 0
all_grade = 0
number_tasks = 0
fail = False
task_name = input()

while order != task_name:
    grade = int(input())
    if grade <= 4:
        number_fails += 1
        if number_fails == eligible_number_fails:
            fail = True
            break
    all_grade += grade
    number_tasks += 1
    name_last_task = task_name
    task_name = input()

if fail:
    print(f'You need a break, {number_fails} poor grades.')
else:
    average_grade = all_grade / number_tasks
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {number_tasks}')
    print(f'Last problem: {name_last_task}')
