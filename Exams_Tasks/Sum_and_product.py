n = int(input())
is_found = False
count = 0

for a in range(1, 9 + 1):
    for b in range(9, a, - 1):
        for c in range(0, 9 + 1):
            for d in range(9, c, - 1):
                num_sum = a + b + c + d
                num_mult = a * b * c * d
                if num_sum == num_mult and n % 100 == 5:
                    count += 1
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                    break
                elif num_mult // num_sum == 3 and n % 3 == 0:
                    count += 1
                    print(f"{d}{c}{b}{a}")
                    is_found = True
                    break

            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

if count == 0:
    print("Nothing found")