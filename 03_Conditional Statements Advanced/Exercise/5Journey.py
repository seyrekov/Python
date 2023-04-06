budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost = budget * 0.3
        vacation = 'Camp'
    elif season == 'winter':
        cost = budget * 0.7
        vacation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost = budget * 0.4
        vacation = 'Camp'
    elif season == 'winter':
        cost = budget * 0.8
        vacation = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    cost = budget * 0.9
    vacation = 'Hotel'
    cost
print(f'Somewhere in {destination}')
print(f'{vacation} - {cost:.2f}')
