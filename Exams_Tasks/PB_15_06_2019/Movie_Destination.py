budget = float(input())
destination = input()
season = input()
days = int(input())
cost = 0

if destination == "Dubai":
    if season == "Winter":
        cost = 45_000
    elif season == "Summer":
        cost = 40_000
elif destination == "Sofia":
    if season == "Winter":
        cost = 17_000
    elif season == "Summer":
        cost = 12_500
elif destination == "London":
    if season == "Winter":
        cost = 24_000
    elif season == "Summer":
        cost = 20_250

total = days * cost

if destination == "Dubai":
    total *= 0.7
elif destination == "Sofia":
    total *= 1.25

diff = abs(budget - total)

if budget > total:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
