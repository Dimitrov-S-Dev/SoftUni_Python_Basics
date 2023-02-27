sea_count = int(input())
mountain_count = int(input())

command = input()
total_sum = 0
is_all_sold = False

while command != "Stop":
    vacation = command
    if vacation == "sea":
        if sea_count > 0:
            sea_count -= 1
            total_sum += 680
    elif vacation == "mountain":
        if mountain_count > 0:
            mountain_count -= 1
            total_sum += 499
    if sea_count == 0 and mountain_count == 0:
        is_all_sold = True
        break
    command = input()


if is_all_sold:
    print("God job! Everything is sold.")

print(f"Profit: {total_sum} lv.")
