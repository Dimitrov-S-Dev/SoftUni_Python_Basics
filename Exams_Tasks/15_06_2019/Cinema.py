capacity = int(input())
total = 0
is_full = False

while True:
    command = input()
    if command == "Movie time!":
        break
    people = int(command)
    if capacity < people:
        is_full = True
        break
    if people % 3 == 0:
        total -= 5
    total += people * 5
    capacity -= people

if is_full:
    print(f"The cinema is full.")
else:
    print(f"There are {capacity} seats left in the cinema.")
print(f"Cinema income - {total} lv.")
