town = input()
sells = float(input())
share_seller = 0

if 0 <= sells <= 500:  # this is equal to using operator AND
    if town == 'Sofia':
        share_seller = sells * 5 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Varna':
        share_seller = sells * 4.5 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Plovdiv':
        share_seller = sells * 5.5 / 100
        print(f'{share_seller:.2f}')
    else:
        print('error')
elif 500 < sells <= 1000:
    if town == 'Sofia':
        share_seller = sells * 7 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Varna':
        share_seller = sells * 7.5 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Plovdiv':
        share_seller = sells * 8 / 100
        print(f'{share_seller:.2f}')
    else:
        print('error')
elif 1000 < sells <= 10000:
    if town == 'Sofia':
        share_seller = sells * 8 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Varna':
        share_seller = sells * 10 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Plovdiv':
        share_seller = sells * 12 / 100
        print(f'{share_seller:.2f}')
    else:
        print('error')
elif sells > 10000:
    if town == 'Sofia':
        share_seller = sells * 12 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Varna':
        share_seller = sells * 13 / 100
        print(f'{share_seller:.2f}')
    elif town == 'Plovdiv':
        share_seller = sells * 14.5 / 100
        print(f'{share_seller:.2f}')
    else:
        print('error')
else:
    print('error')
