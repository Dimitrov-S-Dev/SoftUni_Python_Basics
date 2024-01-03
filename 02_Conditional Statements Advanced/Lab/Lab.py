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
