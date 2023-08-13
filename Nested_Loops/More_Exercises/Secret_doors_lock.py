first_num = int(input())
second_num = int(input())
third_num = int(input())

for i in range(1, first_num + 1):
    if i % 2 != 0:
        continue

    for j in range(2, second_num + 1):
        if j == 4 or j == 6:
            continue

        for k in range(1, third_num + 1):
            if k % 2 != 0:
                continue
            print(f"{i} {j} {k}")
