min_walk = int(input())
numb_of_walks = int(input())
calories = int(input())

total_minutes = min_walk * numb_of_walks
calories_burn = total_minutes * 5
calories *= 0.5

if calories_burn >= calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")
