food_quantity = int(input()) * 1000
consumed_food = 0

while True:
    command = input()
    if command == "Adopted":
        break
    current_food = int(command)
    consumed_food += current_food

diff = abs(food_quantity - consumed_food)
if consumed_food <= food_quantity:
    print(f"Food is enough! Leftovers:{diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
