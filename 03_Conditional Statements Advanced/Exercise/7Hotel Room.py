month = input()
number_nights = int(input())
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 14 >= number_nights > 7:
        studio = studio - studio * 0.05
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
    elif number_nights > 14:
        studio = studio - studio * 0.3
        apartment = apartment - apartment * 0.1
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
    else:
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if number_nights > 14:
        studio = studio - studio * 0.2
        apartment = apartment - apartment * 0.1
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
    else:
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if number_nights > 14:
        apartment = apartment - apartment * 0.1
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
    else:
        cost = number_nights * apartment
        print(f'Apartment: {cost:.2f} lv.')
        cost = number_nights * studio
        print(f'Studio: {cost:.2f} lv.')
