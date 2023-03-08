desi_won_games = 0
desi_lost_games = 0
total_games = 0

while True:
    command = input()
    if command == "End of tournaments":
        break
    tournament = command
    games = int(input())
    total_games += games
    for game in range(1,games + 1):
        desi_team = int(input())
        away_team = int(input())
        diff = abs(desi_team - away_team)
        if desi_team > away_team:
            desi_won_games += 1
            print(f"Game {game} of tournament {tournament}: win with {diff} points.")
        else:
            desi_lost_games += 1
            print(f"Game {game} of tournament {tournament}: lost with {diff} points.")

p_won_g = (desi_won_games / total_games) * 100
p_lost_g = (desi_lost_games / total_games) * 100

print(f"{p_won_g:.2f}% matches win")
print(f"{p_lost_g:.2f}% matches lost")
