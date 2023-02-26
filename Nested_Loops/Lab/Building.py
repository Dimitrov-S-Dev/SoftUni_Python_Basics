floor_count = int(input())
room_count = int(input())

for floor in range(floor_count, 0, -1):
    for room in range(room_count):

        if floor == floor_count:
            letter = "L"
        elif floor % 2 == 0:
            letter = "O"
        else:
            letter = "A"
        print(f"{letter}{floor}{room}",end=" ")
    print()
