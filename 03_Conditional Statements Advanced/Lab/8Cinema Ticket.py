day = (input())

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    price = 12
    print(price)
elif day == 'Wednesday' or day == 'Thursday':
    price = 14
    print(price)
elif day == 'Saturday' or day == 'Sunday':
    price = 16
    print(price)
