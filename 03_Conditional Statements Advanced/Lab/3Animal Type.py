animal_type = str(input())

if animal_type == 'dog':
    print('mammal')
elif animal_type == 'crocodile' or animal_type == 'tortoise' \
        or animal_type == 'snake':
    print('reptile')
elif animal_type != 'mammal' and 'crocodile' and 'tortoise' \
        and 'snake':
    print('unknown')
