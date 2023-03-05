contract = input()
period = input()
internet = input()
months = int(input())
plan = 0

if contract == "one":
    if period == "Small":
        plan = 9.98
    elif period == "Middle":
        plan = 18.99
    elif period == "Large":
        plan = 25.98
    elif period == "ExtraLarge":
        plan = 35.99
elif contract == "two":
    if period == "Small":
        plan = 8.58
    elif period == "Middle":
        plan = 17.09
    elif period == "Large":
        plan = 23.59
    elif period == "ExtraLarge":
        plan = 31.79

if internet == "yes":
    if plan <= 10:
        plan += 5.5
    elif plan <= 30:
        plan += 4.35
    elif plan > 30:
        plan += 3.85

total = plan * months
if contract == "two":
    total *= 0.9625

print(f"{total:.2f} lv.")