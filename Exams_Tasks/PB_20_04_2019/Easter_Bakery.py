flour_price = float(input())
flour_count = float(input())
sugar_count = float(input())
eggs_count = int(input())
yeast_count = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2

total = flour_count * flour_price
total += sugar_count * sugar_price
total += eggs_count * eggs_price
total += yeast_count * yeast_price

print(f"{total:.2f}")
