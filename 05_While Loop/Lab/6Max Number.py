import sys
max_number = -sys.maxsize
text = input()

while text != 'Stop':
    number_input = int(f'{text}')
    if number_input > max_number:
        max_number = number_input
    text = input()
print(max_number)
