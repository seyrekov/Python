product = (input())
town = (input())
quantity = float(input())

if town == 'Sofia':
    if product == 'coffee':
        price = 0.50
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'water':
        price = 0.80
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'beer':
        price = 1.20
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'sweets':
        price = 1.45
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'peanuts':
        price = 1.60
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
elif town == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'water':
        price = 0.70
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'beer':
        price = 1.15
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'sweets':
        price = 1.30
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'peanuts':
        price = 1.50
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
elif town == 'Varna':
    if product == 'coffee':
        price = 0.45
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'water':
        price = 0.70
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'beer':
        price = 1.10
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'sweets':
        price = 1.35
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
    elif product == 'peanuts':
        price = 1.55
        price_quantity = quantity * price
        print(f'{price_quantity:.2f}')
