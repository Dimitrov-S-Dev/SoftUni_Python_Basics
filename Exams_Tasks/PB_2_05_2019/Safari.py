budget = float(input())
petrol = float(input()) * 2.1
day = input()
total = petrol + 100

if day == "Saturday":
    total *= 0.9
elif day == "Sunday":
    total *= 0.8
diff = budget - total
if diff >= 0:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    diff = abs(diff)
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
