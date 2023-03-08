from math import  floor

tournaments = int(input())
start_points = int(input())
points = 0
won_games = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        points += 2000
        won_games += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

final_points = start_points + points
avg_points = floor(points / tournaments)
p_won_games = (won_games / tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {avg_points}")
print(f"{p_won_games:.2f}%")
