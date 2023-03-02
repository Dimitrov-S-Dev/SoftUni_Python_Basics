from math import ceil

people_count = int(input())
entrance_tax = float(input())
sun_bed_price = float(input())
sun_umbrella_price = float(input())

entrance_cost = entrance_tax * people_count
sun_bed_cost = ceil(people_count * 0.75) * sun_bed_price
sun_umbrella_cost = ceil(people_count / 2) * sun_umbrella_price

total = entrance_cost + sun_umbrella_cost + sun_bed_cost

print(f"{total:.2f} lv.")
