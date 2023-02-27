month = input()
hours = int(input())
people_count = int(input())
time_of_the_day = input()
price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price = 10.5
    elif time_of_the_day == "night":
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        price = 12.6
    elif time_of_the_day == "night":
        price = 10.2

if people_count >= 4:
    price *= 0.9
if hours >= 5:
    price *= 0.5


price_per_person = price
print(f"Price per person for one hour: {price:.2f}")

total_price = price_per_person * hours * people_count
print(f"Total cost of the visit: {total_price:.2f}")
