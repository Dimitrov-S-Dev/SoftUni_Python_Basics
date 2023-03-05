strawberries_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

total = strawberries_count * strawberries_price
total += raspberries_count * raspberries_price
total += bananas_count * bananas_price
total += oranges_count * oranges_price
print(f"{total:.2f}")
