initial_score = int(input())

if initial_score <= 100:
    updated_score = 5
elif 1000 >= initial_score > 100:
    updated_score = initial_score * 0.2
elif initial_score > 1000:
    updated_score = initial_score * 0.1

add_updated_score = updated_score

if initial_score % 2 == 0:
    add_updated_score = updated_score + 1
elif initial_score % 5 == 0:
    add_updated_score = updated_score + 2
print(add_updated_score)

all_score = initial_score + add_updated_score

print(all_score)
