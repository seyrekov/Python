movie = input()
rows = int(input())
columns = int(input())

price = 0


if movie == 'Premiere':
    price = 12
elif movie == 'Normal':
    price = 7.50
elif movie == 'Discount':
    price = 5

income = rows * columns
print(f'{price * income:.2f}')
