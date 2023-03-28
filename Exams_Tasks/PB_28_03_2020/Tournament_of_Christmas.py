days = int(input())
money = 0
days_won = 0
days_lose = 0

for day in range(days):
    curr_money = 0
    curr_wins = 0
    curr_lose = 0
    while True:
        game_name = input()
        if game_name == "Finish":
            break
        win_lose = input()
        if win_lose == "win":
            curr_wins += 1
            curr_money += 20
        else:
            curr_lose += 1
    if curr_wins > curr_lose:
        days_won += 1
        curr_money *= 1.1
    else:
        days_lose += 1
    money += curr_money

if days_won > days_lose:
    money *= 1.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")
