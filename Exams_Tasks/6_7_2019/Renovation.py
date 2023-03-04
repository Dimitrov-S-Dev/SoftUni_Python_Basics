from math import ceil
wall_height = int(input())
wal_width = int(input())
percent_not_for_painting = int(input()) / 100
to_paint = ceil(wall_height * wal_width * 4 * (1- percent_not_for_painting))
is_all_painted = False
command = input()

while command != "Tired!":
    litre = int(command)
    to_paint -= litre
    if to_paint <= 0:
        is_all_painted = True
        break

    command = input()

if to_paint > 0:
    print(f"{to_paint} quadratic m left.")
elif is_all_painted and to_paint < 0:
    print(f"All walls are painted and you have {abs(to_paint)} l paint left!")
else:
    print(f"All walls are painted! Great job, Pesho!")
