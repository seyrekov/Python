budget = float(input())
number_statists = int(input())
wardrobe_for_one_statist = float(input())
cost_wardrobe_for_all = wardrobe_for_one_statist * number_statists
decor = budget * 0.10


if number_statists > 150:
    cost_wardrobe_for_all = cost_wardrobe_for_all - \
        cost_wardrobe_for_all * 0.10  # cost_wardrobe_for_all * 0.9

general_costs = cost_wardrobe_for_all + decor

if general_costs > budget:
    shortage_money = general_costs - budget
    print('Not enough money!')
    print(f'Wingard needs {shortage_money:.2f} leva more.')
else:
    balance_money = budget - general_costs
    print('Action!')
    print(f'Wingard starts filming with {balance_money:.2f} leva left.')
