temperature = int(input())
day_period = input()

if day_period == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif temperature >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif day_period == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif 18 < temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif temperature >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif day_period == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    if 10 <= temperature <= 18 or 18 < temperature <= 24 or temperature >= 25:
        print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
