team_won = 0
team_lost = 0
team_draw = 0

for _ in range(3):
    current_game = input()
    home = int(current_game[0])
    away = int(current_game[2])

    if home > away:
        team_won += 1
    elif home < away:
        team_lost += 1
    else:
        team_draw += 1


print(f"Team won {team_won} games.")
print(f"Team lost {team_lost} games.")
print(f"Drawn games: {team_draw}")
