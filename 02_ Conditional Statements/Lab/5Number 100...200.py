number = int(input())
if number < 100:
    print('Less than 100')
elif 100 <= number <= 200:  # elif instead else -> for more than one true/false conditions
    print('Between 100 and 200')
elif number > 200:
    print('Greater than 200')
