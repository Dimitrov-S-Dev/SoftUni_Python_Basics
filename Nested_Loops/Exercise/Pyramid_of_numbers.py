number = int(input())
counter = 1
is_all_printed = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            is_all_printed = True
            break
    if is_all_printed:
        break
    print()
