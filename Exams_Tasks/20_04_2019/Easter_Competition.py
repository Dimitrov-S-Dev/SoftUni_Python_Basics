easter_cakes = int(input())
max_point = 0
max_p_name = ""

for _ in range(easter_cakes):
    cur_points = 0
    baker_name = input()
    while True:
        command = input()
        if command == "Stop":
            break
        points = int(command)
        cur_points += points

    print(f"{baker_name} has {cur_points} points.")
    if cur_points > max_point:
        print(f"{baker_name} is the new number 1!")

    if cur_points > max_point:
        max_point = cur_points
        max_p_name = baker_name

print(f"{max_p_name} won competition with {max_point} points!")
