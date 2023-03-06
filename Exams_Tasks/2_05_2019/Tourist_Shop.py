budget = float(input())
products = 0
total_spent = 0
no_money = False
diff = 0
counter = 0

while True:
    counter += 1
    command = input()
    if command == "Stop":
        break
    product = command
    price = float(input())
    if counter % 3 == 0:
        price *= 0.5
    if price > budget:
        diff += price - budget
        no_money = True
        break
    budget -= price
    products += 1
    total_spent += price

if no_money:
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
else:
    print(f"You bought {products} products for {total_spent:.2f} leva.")
