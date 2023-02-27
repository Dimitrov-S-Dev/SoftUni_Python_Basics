coins_by_one = int(input())
coins_by_two = int(input())
coins_by_five = int(input())
coins_sum = int(input())

for i in range(coins_by_one + 1):
    for j in range(coins_by_two + 1):
        for k in range(coins_by_five + 1):
            if i + (j * 2) + (k * 5) == coins_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {coins_sum} lv.")
