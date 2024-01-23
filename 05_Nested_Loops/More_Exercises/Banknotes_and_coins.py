coins_by_one = int(input())
coins_by_two = int(input())
coins_by_five = int(input())
coins_sum = int(input())

for a in range(coins_by_one + 1):
    for b in range(coins_by_two + 1):
        for c in range(coins_by_five + 1):
            if a + (b * 2) + (c * 5) == coins_sum:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {coins_sum} lv.")
