days_count = int(input())
hours_count = int(input())
total = 0
price = 1

for day in range(1, days_count + 1):
    daily_amount = 0
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        daily_amount += price
    total += daily_amount
    print(f"Day: {day} - {daily_amount:.2f} lv.")

print(f"Total: {total:.2f} lv.")

