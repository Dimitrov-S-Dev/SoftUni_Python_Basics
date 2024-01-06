import sys
from math import floor
# Task 1 Numbers to 1000 Ending on 7

for number in range(1001):
    if number % 10 == 7:
        print(number)

# Task 2 Element Equal to Sum of Rest

n = int(input())
max_num = -sys.maxsize
sum_of_numbers = 0

for _ in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_of_numbers += current_num


if max_num == sum_of_numbers - max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    diffr = abs(max_num - (sum_of_numbers - max_num))
    print("No")
    print(f"Diff = {diffr}")

# Task 3 Histogram

n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(n):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    else:
        p5 += 1

percent_p1 = p1 / n * 100
percent_p2 = p2 / n * 100
percent_p3 = p3 / n * 100
percent_p4 = p4 / n * 100
percent_p5 = p5 / n * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")

# Task 4 Clever Lilly

years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

collected_money = 0
toys_count = 0
money = 10

for year in range(1, years + 1):
    if year % 2 != 0:
        toys_count += 1
    else:
        collected_money += money * (year / 2)

collected_money += toy_price * toys_count
collected_money -= years // 2
diff = abs(collected_money - washing_machine_price)


if collected_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

# Task 5 Salary

open_browsers = int(input())
salary = int(input())


for _ in range(open_browsers):
    current_browser = input()
    if current_browser == "Facebook":
        salary -= 150
    elif current_browser == "Instagram":
        salary -= 100
    elif current_browser == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary")
        break

print(f"{salary:.2f}")

# Task 6 Oscars

actor_name = input()
starting_points = float(input())
number_of_jury = int(input())
actor_points = starting_points
got_nominee = False

for jury in range(number_of_jury):
    jury_name = input()
    current_points = float(input())
    actor_points += (current_points * len(jury_name) / 2)
    if actor_points >= 1250.5:
        print(f"Congratulations, {actor_name} got nominee for leading role with {actor_points}")
        got_nominee = True
        break


if not got_nominee:
    needed_points = 1250.5 - actor_points
    print(f"Sorry, {actor_name} you need {needed_points:.2f} more")

# Task 7 Trekking Mania

number_of_groups = int(input())
musa_ala = 0
mon_bla = 0
kili_manjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(number_of_groups):
    current_people = int(input())
    if current_people <= 5:
        musa_ala += current_people
    elif current_people <= 12:
        mon_bla += current_people
    elif current_people <= 25:
        kili_manjaro += current_people
    elif current_people <= 40:
        k2 += current_people
    else:
        everest += current_people
    total_people += current_people


percent_musa_ala = musa_ala / total_people * 100
percent_mon_bla = mon_bla / total_people * 100
percent_kili_manjaro = kili_manjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musa_ala:.2f}%")
print(f"{percent_mon_bla:.2f}%")
print(f"{percent_kili_manjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

# Task 8 Tennis Ranking

number_of_tournaments = int(input())
starting_points = int(input())
W = 2000
F = 1200
SF = 720
tournament_points = 0
won_tournaments = 0

for _ in range(number_of_tournaments):
    currant_stage = input()
    if currant_stage == "W":
        won_tournaments += 1
        tournament_points += W
    elif currant_stage == "F":
        tournament_points += F
    elif currant_stage == "SF":
        tournament_points += SF

final_points = tournament_points + starting_points
average_tournament_points = floor(tournament_points / number_of_tournaments)
percent_won = won_tournaments / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_tournament_points}")
print(f"{percent_won:.2f}%")
