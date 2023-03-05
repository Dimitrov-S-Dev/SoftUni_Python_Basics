drink = input()
sugar = input()
count_drinks = int(input())

result = 0

if drink == "Espresso":
	if sugar == "Without":
		result = 0.9
	elif sugar == "Normal":
		result = 1
	elif sugar == "Extra":
		result = 1.2
elif drink == "Cappuccino":
	if sugar == "Without":
		result = 1
	elif sugar == "Normal":
		result = 1.2
	elif sugar == "Extra":
		result = 1.6
elif drink == "Tea":
	if sugar == "Without":
		result = 0.5
	elif sugar == "Normal":
		result = 0.6
	elif sugar == "Extra":
		result = 0.7

total = result * count_drinks

if sugar == "Without":
	total *= 0.65
if drink == "Espresso" and count_drinks >= 5:
	total *= 0.75
if total > 15:
	total *= 0.8

print(f"You bought {count_drinks} cups of {drink} for {total:.2f} lv.")
