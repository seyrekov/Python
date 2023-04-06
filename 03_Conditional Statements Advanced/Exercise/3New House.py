flower_kind = input()
number_flower = int(input())
budget = int(input())

if number_flower > 80 and flower_kind == 'Roses':
    roses = 5
    price = number_flower * roses
    discounted_price = price - price * 10 / 100
    if budget >= discounted_price:
        money_left = budget - discounted_price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = discounted_price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
elif not number_flower > 80 and flower_kind == 'Roses':
    roses = 5
    price = number_flower * roses
    if budget >= price:
        money_left = budget - price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')

elif number_flower > 90 and flower_kind == 'Dahlias':
    dahlias = 3.80
    price = number_flower * dahlias
    discounted_price = price - price * 15 / 100
    if budget >= discounted_price:
        money_left = budget - discounted_price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = discounted_price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
elif not number_flower > 90 and flower_kind == 'Dahlias':
    dahlias = 3.80
    price = number_flower * dahlias
    if budget >= price:
        money_left = budget - price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')

if number_flower > 80 and flower_kind == 'Tulips':
    tulips = 2.80
    price = number_flower * tulips
    discount_price = price - price * 15 / 100
    if budget >= discount_price:
        money_left = budget - discount_price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
elif not number_flower > 80 and flower_kind == 'Tulips':
    tulips = 2.80
    price = number_flower * tulips
    if budget >= price:
        money_left = budget - price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')

if number_flower < 120 and flower_kind == 'Narcissus':
    narcissus = 3
    price = number_flower * narcissus
    upper_price = price + price * 15 / 100
    if budget >= upper_price:
        money_left = budget - upper_price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = upper_price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
elif not number_flower < 120 and flower_kind == 'Narcissus':
    narcissus = 3
    price = number_flower * narcissus
    if budget >= price:
        money_left = budget - price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')

if number_flower < 80 and flower_kind == 'Gladiolus':
    gladiolus = 2.50
    price = number_flower * gladiolus
    upper_price = price + price * 20 / 100
    if budget >= upper_price:
        money_left = budget - upper_price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = upper_price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
elif not number_flower < 80 and flower_kind == 'Gladiolus':
    gladiolus = 2.50
    price = number_flower * gladiolus
    if budget >= price:
        money_left = budget - price
        print(
            f'Hey, you have a great garden with {number_flower} {flower_kind} and {money_left:.2f} leva left.')
    else:
        needed_money = price - budget
        print(f'Not enough money, you need {needed_money:.2f} leva more.')
