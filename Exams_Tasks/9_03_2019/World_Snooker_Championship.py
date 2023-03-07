stage = input()
ticket = input()
ticket_count = int(input())
photo = input()
price = 0

if stage == "Quarter final":
    if ticket == "Standard":
        price = 55.5
    elif ticket == "Premium":
        price = 105.2
    elif ticket == "VIP":
        price = 118.9
elif stage == "Semi final":
    if ticket == "Standard":
        price = 75.88
    elif ticket == "Premium":
        price = 125.22
    elif ticket == "VIP":
        price = 300.4
elif stage == "Final":
    if ticket == "Standard":
        price = 110.1
    elif ticket == "Premium":
        price = 160.66
    elif ticket == "VIP":
        price = 400

total = price * ticket_count


if total > 4000:
    total *= 0.75
elif total > 2500:
    total *= 0.9
    if photo == "Y":
        total += 40 * ticket_count
else:
    if photo == "Y":
        total += 40 * ticket_count

print(f"{total:.2f}")
