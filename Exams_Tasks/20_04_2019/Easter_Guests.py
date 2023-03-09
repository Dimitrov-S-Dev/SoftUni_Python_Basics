from math import ceil

guests = int(input())
budget = float(input())

cake_count = ceil(guests / 3)
eggs_count = guests * 2
cake_price = cake_count * 4
eggs_price = eggs_count * 0.45
total = cake_price + eggs_price
diff = abs(budget - total)

if budget >= total:
    print(f"Lyubo bought {cake_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
