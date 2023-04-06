number_one = int(input())
number_two = int(input())

for c_n in range(number_one, number_two + 1):
    odd_num_s = 0
    even_num_s = 0
    num_as_text = str(c_n)
    for index, n in enumerate(num_as_text):
        if index % 2 == 0:
            odd_num_s += int(n)
        else:
            even_num_s += int(n)
    if even_num_s == odd_num_s:
        print(c_n, end=' ')
