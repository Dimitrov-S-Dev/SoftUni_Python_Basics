days = int(input())
food = float(input())
dog = 0
cat = 0
biscuits = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    if day % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1
    dog += dog_food
    cat += cat_food

total = dog + cat
perc_food = (total / food ) * 100
perc_dog = (dog / total) * 100
cat_perc = (cat / total) * 100
print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{perc_food:.2f}% of the food has been eaten.")
print(f"{perc_dog:.2f}% eaten from the dog.")
print(f"{cat_perc:.2f}% eaten from the cat.")
