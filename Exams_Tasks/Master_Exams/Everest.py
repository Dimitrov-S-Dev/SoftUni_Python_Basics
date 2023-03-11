start = 5364
end = 8848

command = input()
days = 1
is_pck_rich = False
condition = False

while command != "END":
    action = command

    if action == "Yes":
        meters = int(input())
        start += meters
        days += 1
        if days > 5:
            break

    elif action == "No":
        meters = int(input())
        start += meters

    if start >= end:
        is_pck_rich = True
        break
    command = input()


if is_pck_rich:
    print(f"Goal reached for {days} days!")
else:
    print("Failed")
    print(start)
