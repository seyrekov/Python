n_tab = int(input())
salary = int(input())
sum_penalties = 0
penalty_f = 0
penalty_i = 0
penalty_r = 0
for website in range(n_tab):
    n_name_website = input()
    if n_name_website == 'Facebook':
        penalty_f += 150
    elif n_name_website == 'Instagram':
        penalty_i += 100
    elif n_name_website == 'Reddit':
        penalty_r += 50
    sum_penalties = penalty_f + penalty_i + penalty_r

left = salary - sum_penalties
if left <= 0:
    print('You have lost your salary.')
else:
    print(f'{left}')
