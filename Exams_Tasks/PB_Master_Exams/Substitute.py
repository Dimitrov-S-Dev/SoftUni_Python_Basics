k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0
is_finish = False

for first in range(k, 9):
    for second in range(9,l - 1, -1):
        for third in range(m, 9):
            for forth in range(9, n - 1, -1):
                if (first % 2 == 0 and third % 2 == 0) and (second % 2 != 0 and forth % 2 !=0):
                    if first == third and second == forth:
                        print(f"Cannot change the same player")
                        continue
                    else:
                        count += 1
                        print(f"{first}{second} - {third}{forth}")
            if count == 6:
                is_finish = True
                break
        if is_finish:
            break
    if is_finish:
        break
