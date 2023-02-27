people_count = int(input())
season = input()
price = 0

if people_count <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.5
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86
else:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45
    elif season == "autumn":
        price = 49.5
    elif season == "winter":
        price = 85


price = price * people_count

if season == "summer":
    price *= 0.85
elif season == "winter":
    price *= 0.92

print(f"{price:.2f}")
