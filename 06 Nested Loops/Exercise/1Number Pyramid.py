fin_number = int(input())
counter = 1
task_done = False

for row in range(1, fin_number + 1):
    for column in range(1, row + 1):
        print(counter, end=' ')
        counter += 1
        if counter > fin_number:
            task_done = True
            break
    if task_done:
        break
    print()
