from math import ceil

days = int(input())
food_left = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

deer_per_day = first_deer_food + second_deer_food + third_deer_food

total_deer_food = deer_per_day * days

diff = abs(total_deer_food - food_left)
if total_deer_food <= food_left:
    print(f"{ceil(diff)} kilos food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed")
