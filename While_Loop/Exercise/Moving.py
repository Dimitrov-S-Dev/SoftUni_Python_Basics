space_width = int(input())
space_length = int(input())
space_height = int(input())
space_volume = space_height * space_length * space_width

command = input()
is_have_space = True

while command != "Done":
    current_box = int(command)
    space_volume -= current_box
    if space_volume < 0:
        is_have_space = False
        break
    command = input()


if is_have_space:
    print(f"{space_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_volume)} Cubic meters more.")
