name = input()
pack = input()
tickets = int(input())
price = 0

if name == "John Wick":
    if pack == "Drink":
        price = 12
    elif pack == "Popcorn":
        price = 15
    elif pack == "Menu":
        price = 19
elif name == "Star Wars":
    if pack == "Drink":
        price = 18
    elif pack == "Popcorn":
        price = 25
    elif pack == "Menu":
        price = 30
elif name == "Jumanji":
    if pack == "Drink":
        price = 9
    elif pack == "Popcorn":
        price = 11
    elif pack == "Menu":
        price = 14

total = price * tickets

if name == "Star Wars" and tickets >= 4:
    total *= 0.7
if name == "Jumanji" and tickets == 2:
    total *= 0.85

print(f"Your bill is {total:.2f} leva.")
