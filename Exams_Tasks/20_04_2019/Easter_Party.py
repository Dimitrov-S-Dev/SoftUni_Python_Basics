guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_person *= 0.85
elif 15 < guests <= 20:
    price_per_person *= 0.8
elif guests > 20:
    price_per_person *= 0.75

cake_price = budget * 0.1
total = price_per_person * guests + cake_price
diff = abs(budget - total)

if budget >= total:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
