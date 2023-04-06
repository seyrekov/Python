import sys
min_value = sys.maxsize
text_input = input()

while text_input != 'Stop':
    number = int(f'{text_input}')
    if number < min_value:
        min_value = number
    text_input = input()
print(min_value)
