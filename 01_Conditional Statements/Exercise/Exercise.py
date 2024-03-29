import math

# Task 1 Seconds Sum

first = int(input())
second = int(input())
third = int(input())

total = first + second + third
minutes = total // 60
seconds = total % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

# Task 2 Bonus Points

starting_points = int(input())
bonus_points = None

if starting_points <= 100:
    bonus_points = 5
elif starting_points > 1000:
    bonus_points = starting_points * 0.1
else:
    bonus_points = starting_points * 0.2

if starting_points % 2 == 0:
    bonus_points += 1
elif starting_points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(bonus_points + starting_points)

# Task 3 Time + 15 minutes

hour = int(input())
minutes = int(input())
minutes = hour * 60 + (minutes + 15)
hour_result = minutes // 60
minutes_result = minutes % 60

if hour_result > 23:
    hour_result -= 24

print(f"{hour_result}:{minutes_result:02d}")

# Task 4 Toy Store

puzzle_price = 2.6
dull_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

trip_price = float(input())
puzzle_count = int(input())
dull_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

collected_money = puzzle_count * puzzle_price + dull_count * dull_price +\
                  bear_count * bear_price + minion_count * minion_price + \
                  truck_count * truck_price

toys_count = puzzle_count + dull_count + bear_count + minion_count + truck_count

if toys_count >= 50:
    collected_money *= 0.75

collected_money_after_rent = collected_money * 0.9
money_left = abs(collected_money_after_rent - trip_price)

if collected_money_after_rent >= trip_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")


# Task 5 Godzilla vs Kong

budget = float(input())
statist_count = int(input())
single_costume_price = float(input())
decor = budget * 0.1

if statist_count > 150:
    single_costume_price *= 0.9

total = decor + (statist_count * single_costume_price)

money_left = abs(budget - total)

if total <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")

# Task 6 Swimming World record

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())

water_resistance = (distance_in_meters // 15) * 12.5
swimmer_seconds = seconds_for_one_meter * distance_in_meters + water_resistance

if swimmer_seconds >= record_in_seconds:
    print(f"No, he failed! He was {swimmer_seconds - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {swimmer_seconds:.2f} seconds.")

# Task 7 Shopping

budget = float(input())

video_card_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_card_price = video_card_count * 250
processors_price = processors_count * video_card_price * 0.35
ram_price = ram_count * video_card_price * 0.1

price = video_card_price + processors_price + ram_price
if video_card_count > processors_count:
    price *= 0.85

if price <= budget:
    print(f"You have {budget - price:.2f} leva left!")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva more!")

# Task 8 Lunch Break

movie_name = input()
movie_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
time_left = break_time - (lunch_time + rest_time)

time_left_formatted = abs(math.ceil(movie_length - time_left))

if time_left >= movie_length:
    print(f"You have enough time to watch {movie_name} and left with {int(time_left_formatted)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {int(time_left_formatted)} more minutes.")
