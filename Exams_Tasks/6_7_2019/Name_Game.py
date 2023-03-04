max_points = 0
winner_name = ""

while True:
    points = 0
    name = input()
    if name == "Stop":
        break

    for index in range(len(name)):
        word = chr(int(input()))
        if word == name[index]:
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        winner_name = name

print(f"The winner is {winner_name} with {max_points} points!")
