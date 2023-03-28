fruit = input()
size = input()
count = int(input())
price = 0

if fruit == "Watermelon":
    if size == "small":
        price = 56 * 2
    elif size == "big":
        price = 28.7 * 5
elif fruit == "Mango":
    if size == "small":
        price = 36.66 * 2
    elif size == "big":
        price = 19.6 * 5
elif fruit == "Pineapple":
    if size == "small":
        price = 42.1 * 2
    elif size == "big":
        price = 24.8 * 5
elif fruit == "Raspberry":
    if size == "small":
        price = 20 * 2
    elif size == "big":
        price = 15.2 * 5

total = price * count
if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5

print(f"{total:.2f} lv.")
