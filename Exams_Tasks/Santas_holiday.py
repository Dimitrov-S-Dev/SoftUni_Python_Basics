days_stay = int(input()) - 1
room_type = input()
feedback = input()
discount = 1

if room_type == "apartment":
    price = 25
    if days_stay < 10:
        discount = 0.7
    elif days_stay <= 15:
        discount = 0.65
    else:
        discount = 0.5
elif room_type == "president apartment":
    price = 35
    if days_stay < 10:
        discount = 0.9
    elif days_stay <= 15:
        discount = 0.85
    else:
        discount = 0.8
else:
    price = 18

total = price * discount * days_stay

if feedback == "positive":
    total *= 1.25
elif feedback == "negative":
    total *= 0.9

print(f"{total:.2f}")
