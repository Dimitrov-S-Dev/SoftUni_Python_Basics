team_name = input()
number_of_games = int(input())
points = 0
w, d, l = 0, 0, 0
for _ in range(number_of_games):
    output = input()
    if output == "W":
        points += 3
        w += 1
    elif output == "D":
        points += 1
        d += 1
    else:
        l += 1

if number_of_games > 0:
    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    win_rate = (w / number_of_games) * 100
    print(f"Win rate: {win_rate:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")
