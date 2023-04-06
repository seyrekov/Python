n = int(input())
for num in range(1111, 9999 + 1):
    spec_n = True
    num_text = str(num)
    for digit in num_text:
        if int(digit) == 0 or n % int(digit) != 0:
            spec_n = False
            break
    if spec_n:
        print(num, end=' ')
