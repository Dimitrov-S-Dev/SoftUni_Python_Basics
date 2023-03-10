from math import ceil

easter_cakes = int(input())
sugar = 0
flour = 0
max_sugar = 0
max_flour = 0

for _ in range(easter_cakes):
    cur_sugar = int(input())
    cur_flour = int(input())
    if cur_sugar > max_sugar:
        max_sugar = cur_sugar
    if cur_flour > max_flour:
        max_flour = cur_flour
    sugar += cur_sugar
    flour += cur_flour

s_packs = ceil(sugar / 950)
f_packs = ceil(flour / 750)

print(f"Sugar: {s_packs}")
print(f"Flour: {f_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
