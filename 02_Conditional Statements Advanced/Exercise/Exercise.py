# Task 1 Cinema

# premier_price = 12
# normal_price = 7.5
# discount_price = 5.0
#
# cinema_type = input()
# rows = int(input())
# cols = int(input())
# price = None
#
# if cinema_type == "Premiere":
#     price = premier_price
# elif cinema_type == "Normal":
#     price = normal_price
# elif cinema_type == "Discount":
#     price = discount_price
#
# result = rows * cols * price
# print(f"{result:.2f} leva")

# Task 2 Summer Outfit

# celsius = int(input())
# time_of_the_day = input()
#
# Outfit = None
# Shoes = None
#
# if 10 <= celsius <= 18:
#     if time_of_the_day == "Morning":
#         Outfit = "Sweatshirt"
#         Shoes = "Sneakers"
#     elif time_of_the_day == "Afternoon":
#         Outfit = "Shirt"
#         Shoes = "Moccasins"
#     else:
#         Outfit = "Shirt"
#         Shoes = "Moccasins"
# elif 18 < celsius <= 24:
#     if time_of_the_day == "Morning":
#         Outfit = "Shirt"
#         Shoes = "Moccasins"
#     elif time_of_the_day == "Afternoon":
#         Outfit = "T-Shirt"
#         Shoes = "Sandals"
#     else:
#         Outfit = "Shirt"
#         Shoes = "Moccasins"
# else:
#     if time_of_the_day == "Morning":
#         Outfit = "T-Shirt"
#         Shoes = "Sandals"
#     elif time_of_the_day == "Afternoon":
#         Outfit = "Swim Suit"
#         Shoes = "Barefoot"
#     else:
#         Outfit = "Shirt"
#         Shoes = "Moccasins"
# print(f"It's {celsius} degrees, get your {Outfit} and {Shoes}.")

# Task 3 New House

# flower_type = input()
# flower_count = int(input())
# budget = int(input())
#
# Roses = 5
# Dahlias = 3.8
# Tulips = 2.8
# Narcissus = 3
# Gladiolus = 2.5
# price = 0
#
# if flower_type == "Roses":
#     price = flower_count * Roses
#     if flower_count > 80:
#         price = 0.9 * flower_count * Roses
# elif flower_type == "Dahlias":
#     price = flower_count * Dahlias
#     if flower_count > 90:
#         price = 0.85 * flower_count * Dahlias
# elif flower_type == "Tulips":
#     price = flower_count * Tulips
#     if flower_count > 80:
#         price = 0.85 * flower_count * Tulips
# elif flower_type == "Narcissus":
#     price = flower_count * Narcissus
#     if flower_count < 120:
#         price = 1.15 * flower_count * Narcissus
# elif flower_type == "Gladiolus":
#     price = flower_count * Gladiolus
#     if flower_count < 80:
#         price = 1.2 * flower_count * Gladiolus
#
# if budget >= price:
#     print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - price:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {price - budget:.2f} leva more.")

# Task 4 Fishing Boat

# budget = int(input())
# season = input()
# fishers = int(input())
#
# ship_rent_spring = 3000
# ship_rent_summer_aunt = 4200
# ship_rent_winter = 2600
# price = 0
#
# if season == "Spring":
#     price = 3000
#     if fishers <= 6:
#         price *= 0.9
#     elif 7 <= fishers <= 11:
#         price *= 0.85
#     else:
#         price *= 0.75
# elif season == "Summer" or season == "Autumn":
#     price = 4200
#     if fishers <= 6:
#         price *= 0.9
#     elif 7 <= fishers <= 11:
#         price *= 0.85
#     else:
#         price *= 0.75
# elif season == "Winter":
#     price = 2600
#     if fishers <= 6:
#         price *= 0.9
#     elif 7 <= fishers <= 11:
#         price *= 0.85
#     else:
#         price *= 0.75
#
# if fishers % 2 == 0 and season != "Autumn":
#     price *= 0.95
#
# if budget >= price:
#     print(f"Yes! You have {budget - price:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {price - budget:.2f} leva.")


# Task 5 Journey

# budget = float(input())
# season = input()
#
# destination = None
# place = None
#
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         place = "Camp"
#         budget *= 0.3
#     elif season == "winter":
#         place = "Hotel"
#         budget *= 0.7
# elif 100 <= budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         place = "Camp"
#         budget *= 0.4
#     elif season == "winter":
#         place = "Hotel"
#         budget *= 0.8
# else:
#     place = "Hotel"
#     destination = "Europe"
#     budget *= 0.9
# print(f"Somewhere in {destination}")
# print(f"{place} - {budget:.2f}")

# Task 6 Operations Between Numbers

# num_1 = int(input())
# num_2 = int(input())
# operator = input()
#
# result = None
#
# if operator == "+":
#     result = f"{num_1} + {num_2} = {num_1 + num_2}" + (" - even" if (num_1 + num_2) % 2 == 0 else " - odd")
# elif operator == "-":
#     result = f"{num_1} - {num_2} = {num_1 - num_2}" + (" - even" if (num_1 - num_2) % 2 == 0 else " - odd")
# elif operator == "*":
#     result = f"{num_1} * {num_2} = {num_1 * num_2}" + (" - even" if (num_1 * num_2) % 2 == 0 else " - odd")
# elif num_2 == 0:
#     result = f"Cannot divide {num_1} by zero"
# elif operator == "/":
#     result = f"{num_1} / {num_2} = {num_1 / num_2:.2f}"
# elif operator == "%":
#     result = f"{num_1} % {num_2} = {num_1 % num_2}"
#
# print(result)