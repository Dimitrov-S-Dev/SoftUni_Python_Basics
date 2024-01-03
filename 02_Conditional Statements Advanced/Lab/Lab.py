# Task 1 Day of Week

# day_of_week = int(input())
#
# if day_of_week == 1:
#     print("Monday")
# elif day_of_week == 2:
#     print("Tuesday")
# elif day_of_week == 3:
#     print("Wednesday")
# elif day_of_week == 4:
#     print("Thursday")
# elif day_of_week == 5:
#     print("Friday")
# elif day_of_week == 6:
#     print("Saturday")
# elif day_of_week == 7:
#     print("Sunday")
# else:
#     print("Error")

# Task 2 Weekend or Working Day

day = (input())

if day == "Monday" \
        or day == "Tuesday" \
        or day == "Wednesday" \
        or day == "Thursday" \
        or day == "Friday":
    print("Working day")
elif day == "Saturday" \
        or day == "Sunday":
    print("Weekend")
else:
    print("Error")

# Task 3 Animal Type

animal = input()

if animal == "dog":
    print("mammal")
elif animal == "snake" \
      or animal == "crocodile" \
      or animal == "tortoise":
    print("reptile")
else:
    print("unknown")

# Task 4 Personal Titles

age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

# Task 5 Small Shop

product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.5
        print(quantity * price)
    elif product == "water":
        price = 0.8
        print(quantity * price)
    elif product == "beer":
        price = 1.2
        print(quantity * price)
    elif product == "sweets":
        price = 1.45
        print(quantity * price)
    elif product == "peanuts":
        price = 1.6
        print(quantity * price)

if city == "Plovdiv":
    if product == "coffee":
        price = 0.4
        print(quantity * price)
    elif product == "water":
        price = 0.7
        print(quantity * price)
    elif product == "beer":
        price = 1.15
        print(quantity * price)
    elif product == "sweets":
        price = 1.30
        print(quantity * price)
    elif product == "peanuts":
        price = 1.5
        print(quantity * price)

if city == "Varna":
    if product == "coffee":
        price = 0.45
        print(quantity * price)
    elif product == "water":
        price = 0.7
        print(quantity * price)
    elif product == "beer":
        price = 1.1
        print(quantity * price)
    elif product == "sweets":
        price = 1.35
        print(quantity * price)
    elif product == "peanuts":
        price = 1.55
        print(quantity * price)

# Task 6 Number in Range

num = int(input())

if -100 <= num <= 100 and num != 0:
    print("Yes")
else:
    print("No")

# Task 7 Working Hours

hour = int(input())
day_of_week = input()

if 10 <= hour <= 18 and day_of_week != "Sunday":
    print("open")
else:
    print("closed")
