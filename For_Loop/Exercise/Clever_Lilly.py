years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

collected_money = 0
toys_count = 0
money = 0

for year in range(1, years + 1):
    if year % 2 != 0:
        toys_count += 1
    else:
        money += 10
        collected_money += money - 1


collected_money += toy_price * toys_count
diff = abs(collected_money - washing_machine_price)

if collected_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
