command = input()
max_goals = 0
max_goals_name = ""
is_have_hat_trick = False

while command != "END":
    player_name = command
    scored_goals = int(input())
    if scored_goals > max_goals:
        max_goals = scored_goals
        max_goals_name = player_name
        if scored_goals >= 3:
            is_have_hat_trick = True
    if scored_goals >= 10:
        break
    command = input()

print(f"{max_goals_name} is the best player!")


if is_have_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick!!!")
else:
    print(f"He has scored {max_goals} goals.")
