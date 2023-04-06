needed_money = float(input())
owned_money = float(input())
sum_money = 0
days_spent = 0
all_days = 0
ready_money_for_vacation = False

while owned_money < needed_money and days_spent < 5:
    action = input()
    sum_money = float(input())
    all_days += 1
    if action == 'save':
        owned_money += sum_money
        days_spent = 0
        if owned_money >= needed_money:
            ready_money_for_vacation = True
            break

    elif action == 'spend':
        owned_money -= sum_money
        days_spent += 1
        if owned_money < 0:
            owned_money = 0
        if days_spent >= 5:
            ready_money_for_vacation = False
            break

if ready_money_for_vacation:
    print(f'You saved the money for {all_days} days.')
else:
    print("You can't save the money.")
    print(f'{all_days}')
