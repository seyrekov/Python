n = int(input())
# 2x0,2x2,2x4...depends how many even degrees we have in n, step is the degree
for number in range(0, n+1, 2):
    print(pow(2, number))  # which degree, which variable
