destination_country = input()
cash_needed = 0
budget = 0

while destination_country != 'End':
    budget = float(input())
    cash_needed = 0
    while cash_needed < budget:
        cash = float(input())
        cash_needed += cash
        if cash_needed >= budget:
            print(f'Going to {destination_country}!')

    destination_country = input()
