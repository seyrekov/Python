debit = input()
whole_sum = 0

while debit != 'NoMoreMoney':
    debit_num = float(f'{debit}')

    if debit_num > 0:
        print(f'Increase: {debit_num:.2f}')
        whole_sum += debit_num
    else:
        print('Invalid operation!')
        break
    debit = input()
print(f'Total: {whole_sum:.2f}')
