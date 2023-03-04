budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extras = int(input()) / 100

if nights > 7:
	price_per_night *= 0.95

total_cost = nights * price_per_night
budget *= (1 - percent_extras)

if budget >= total_cost:
	print(f"Ivanovi will be left with {budget - total_cost:.2f} leva after vacation.")
else:
	print(f"{total_cost - budget:.2f} leva needed.")
