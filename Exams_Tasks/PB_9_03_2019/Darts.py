player_name = input()
points = 301
good_shot = 0
is_won = False
count = 0

while True:
    command = input()
    if command == "Retire":
        break
    count += 1
    pole = command
    c_point = int(input())

    if pole == "Double":
        c_point *= 2
    elif pole == "Triple":
        c_point *= 3
    if c_point <= points:
        points -= c_point
        good_shot += 1
    if points == 0:
        is_won = True
        break

if is_won:
    print(f"{player_name} won the leg with {good_shot} shots.")
else:
    diff = count - good_shot
    print(f"{player_name} retired after {diff} unsuccessful shots.")
