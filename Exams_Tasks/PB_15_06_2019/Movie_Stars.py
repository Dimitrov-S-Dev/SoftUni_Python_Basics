budget = float(input())
is_budget_over = False

while True:
    command = input()
    if command == "ACTION":
        break
    name = command
    if len(name) > 15:
        payment = budget * 0.2
    else:
        payment = float(input())
    budget -= payment

    if budget <= 0:
        is_budget_over = True
        break

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
