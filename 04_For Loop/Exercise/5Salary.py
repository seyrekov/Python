n_tab = int(input())
salary = int(input())
still_have_salary = True

for website in range(n_tab):
    n_name_website = input()
    if n_name_website == 'Facebook':
        salary -= 150
    elif n_name_website == 'Instagram':
        salary -= 100
    elif n_name_website == 'Reddit':
        salary -= 50
    if salary <= 0:
        still_have_salary = False
        break

if still_have_salary:
    print(f'{salary}')
else:
    print('You have lost your salary.')
