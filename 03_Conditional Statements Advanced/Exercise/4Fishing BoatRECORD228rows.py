budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == 'Spring':
    rent = 3000
    if fishermen <= 6:
        discount = rent * 0.10
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 7 <= fishermen <= 11:
        discount = rent * 0.15
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif fishermen >= 12:
        discount = rent * 0.25
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
elif season == 'Summer':
    rent = 4200
    if fishermen <= 6:
        discount = rent * 0.10
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    if 7 <= fishermen <= 11:
        discount = rent * 0.15
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    if fishermen >= 12:
        discount = rent * 0.25
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
elif season == 'Autumn':
    rent = 4200
    if fishermen <= 6:
        discount = rent * 0.10
        price = rent - discount
        if budget >= price:
            left_money = abs(budget - price)
            print(f'Yes! You have {left_money:.2f} leva left.')
        else:
            not_enough_money = abs(budget - price)
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    if 7 <= fishermen <= 11:
        discount = rent * 0.15
        price = rent - discount
        if budget >= price:
            left_money = abs(budget - price)
            print(f'Yes! You have {left_money:.2f} leva left.')
        else:
            not_enough_money = abs(budget - price)
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    if fishermen >= 12:
        discount = rent * 0.25
        price = rent - discount
        if budget >= price:
            left_money = abs(budget - price)
            print(f'Yes! You have {left_money:.2f} leva left.')
        else:
            not_enough_money = abs(budget - price)
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
elif season == 'Winter':
    rent = 2600
    if fishermen <= 6:
        discount = rent * 0.10
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    if 7 <= fishermen <= 11:
        discount = rent * 0.15
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
    if fishermen >= 12:
        discount = rent * 0.25
        price = rent - discount
        if fishermen % 2 == 0:
            discount_two = price * 0.05
            price_discounted = price - discount_two
            if budget >= price_discounted:
                left_money = abs(budget - price_discounted)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price_discounted)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
        else:
            if budget >= price:
                left_money = abs(budget - price)
                print(f'Yes! You have {left_money:.2f} leva left.')
            else:
                not_enough_money = abs(budget - price)
                print(
                    f'Not enough money! You need {not_enough_money:.2f} leva.')
