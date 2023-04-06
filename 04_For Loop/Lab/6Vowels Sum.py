text = input()
value = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0

for letter in text:
    if letter == 'a':
        value = 1
        number1 = text.count(letter) * value
    if letter == 'e':
        value = 2
        number2 = text.count(letter) * value
    if letter == 'i':
        value = 3
        number3 = text.count(letter) * value
    if letter == 'o':
        value = 4
        number4 = text.count(letter) * value
    if letter == 'u':
        value = 5
        number5 = text.count(letter) * value
    else:
        value = 0
number = number1 + number2 + number3 + number4 + number5
print(number)
