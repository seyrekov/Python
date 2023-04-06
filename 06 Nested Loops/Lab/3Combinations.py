n = int(input())
x1 = 0
x2 = 0
x3 = 0

solution = 0

for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            final_match = x1 + x2 + x3
            if final_match == n:
                solution += 1
print(f'{solution}')
