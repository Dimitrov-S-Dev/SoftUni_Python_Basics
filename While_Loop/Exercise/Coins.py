money = float(input())
coins = int(money * 100)
coins_count = 0

while coins:
    if coins >= 200:
        coins_count += coins // 200
        coins = coins % 200
    elif coins >= 100:
        coins_count += coins // 100
        coins = coins % 100
    elif coins >= 50:
        coins_count += coins // 50
        coins = coins % 50
    elif coins >= 20:
        coins_count += coins // 20
        coins = coins % 20
    elif coins >= 10:
        coins_count += coins // 10
        coins = coins % 10
    elif coins >= 5:
        coins_count += coins // 5
        coins = coins % 5
    elif coins >= 2:
        coins_count += coins // 2
        coins = coins % 2
    elif coins >= 1:
        coins_count += coins // 1
        coins = coins % 1

print(coins_count)

