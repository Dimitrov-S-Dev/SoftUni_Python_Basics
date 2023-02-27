needed_money = float(input())
money_in_hand = float(input())
spending_days = 0
days = 0
is_only_spending = False

while True:
    days += 1
    action = input()
    amount = float(input())
    if action == "save":
        spending_days = 0
        money_in_hand += amount
        if money_in_hand >= needed_money:
            break
    else:
        spending_days += 1
        if spending_days == 5:
            print(f"You cant save the money.")
            print(days)
            is_only_spending = True
            break


if not is_only_spending:
    print(f"You saved the money for {days} days.")
