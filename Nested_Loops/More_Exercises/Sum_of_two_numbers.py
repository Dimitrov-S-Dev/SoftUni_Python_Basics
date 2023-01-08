start = int(input())
end = int(input())
magic_number = int(input())
comb = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        comb += 1
        if i + j == magic_number:
            print(f"Combination N:{comb}")
            print(f"({i} + {j} = {magic_number})")
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f"{comb} combinations - neither equals {magic_number}")
