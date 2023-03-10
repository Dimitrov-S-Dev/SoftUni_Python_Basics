price_over_20 = float(input())
kilograms = float(input())
days = int(input())
luggage = int(input())

if kilograms < 10:
    price_over_20 *= 0.2
elif kilograms <= 20:
    price_over_20 *= 0.5

if days < 7:
    price_over_20 *= 1.4
elif days <= 30:
    price_over_20 *= 1.15
else:
    price_over_20 *= 1.1

total = price_over_20 * luggage
print(f" The total price of bags is: {total:.2f} lv. ")
