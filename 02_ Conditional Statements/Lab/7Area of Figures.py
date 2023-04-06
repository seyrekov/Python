from math import pi
figure = (input())

if figure == 'square':
    side_a = float(input())
    print(f'{side_a * side_a:.3f}')
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    print(f'{side_a * side_b:.3f}')
elif figure == 'circle':
    rad = float(input())
    print(f'{pi * rad * rad:.3f}')
elif figure == 'triangle':
    side_a = float(input())
    height_a = float(input())
    print(f'{side_a * height_a / 2:.3f}')
