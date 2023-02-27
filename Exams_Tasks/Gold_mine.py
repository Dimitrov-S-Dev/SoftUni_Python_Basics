location_count = int(input())

for location in range(location_count):
    expected_avr_per_day = float(input())
    days_to_dig = int(input())
    location_gold = 0
    for day in range(days_to_dig):
        current_gold = float(input())
        location_gold += current_gold

    avr_location = location_gold / days_to_dig

    if avr_location >= expected_avr_per_day:
        print(f"Good job! Average gold per day: {avr_location:.2f}")
    else:
        diff = expected_avr_per_day - avr_location
        print(f"You need {diff:.2f} gold.")
