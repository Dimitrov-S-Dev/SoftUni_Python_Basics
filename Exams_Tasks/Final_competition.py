dancers = int(input())
points = float(input())
season = input()
location = input()
total = 0

if location == "Bulgaria":
    total = dancers * points
elif location == "abroad":
    total = dancers * points * 1.5

if season == "summer":
    if location == "bulgaria":
        total *= 0.95
    elif location == "abroad":
        total *= 0.9
elif season == "winter":
    if location == "Bulgaria":
        total *= 0.92
    elif location == "Abroad":
        total *= 0.85


money_for_charity = total * 0.75
money_per_dancer = (total - money_for_charity) / dancers

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
