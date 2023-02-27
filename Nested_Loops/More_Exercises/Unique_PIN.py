first_num = int(input())
second_num = int(input())
third_num = int(input())

for first_digit in range(1, first_num + 1):
    if first_digit % 2 != 0:
        continue

    for second_digit in range(2, second_num + 1):
        if second_digit == 4 or second_digit == 6:
            continue
        for third_digit in range(2, third_num + 1):
            if third_digit % 2 != 0:
                continue

            print(f"{first_digit} {second_digit} {third_digit}")

