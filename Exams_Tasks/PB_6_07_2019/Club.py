wished_profit = float(input())
amount_due = 0
cocktail_price = 0


while amount_due < wished_profit:
	cocktail_name = input()
	if cocktail_name == "Party!":
		break
	cocktails_order = int(input())
	cocktail_price = cocktails_order * len(cocktail_name)
	if cocktail_price % 2 != 0:
		cocktail_price *= 0.75
	amount_due += cocktail_price

if wished_profit > amount_due:
	print(f"We need {wished_profit - amount_due:.2f} leva more.")
else:
	print(f"Target acquired.")
print(f"Club income - {amount_due:.2f} leva.")
