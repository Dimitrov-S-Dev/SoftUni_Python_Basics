city = input()
package = input()
discount_card = input()
days = int(input())

price = 0
is_invalid = False

if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        price = 100
        if discount_card == "yes":
            price *= 0.9
    elif package == "noEquipment":
        price = 80
        if discount_card == "yes":
            price *= 0.95
    else:
        is_invalid = True
elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        price = 130
        if discount_card == "yes":
            price *= 0.88
    elif package == "noBreakfast":
        price = 100
        if discount_card == "yes":
            price *= 0.93
    else:
        is_invalid = True
else:
    is_invalid = True

if is_invalid:
    print("Invalid input!")
elif days <= 0:
    print(f"Days must be positive number!")
else:
    if days > 7:
        days -= 1
    total = price * days
    print(f"The price is {total:.2f}lv! Have a nice time!")
