from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
W = 2000
F = 1200
SF = 720
tournament_points = 0
won_tournaments = 0

for _ in range(number_of_tournaments):
    currant_stage = input()
    if currant_stage == "W":
        won_tournaments += 1
        tournament_points += W
    elif currant_stage == "F":
        tournament_points += F
    elif currant_stage == "SF":
        tournament_points += SF

final_points = tournament_points + starting_points
average_tournament_points = floor(tournament_points / number_of_tournaments)
percent_won = won_tournaments / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_tournament_points}")
print(f"{percent_won:.2f}%")
