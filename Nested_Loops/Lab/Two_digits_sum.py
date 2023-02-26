start = int(input())
end = int(input())
magic_num = int(input())
comb = 0
is_have_comb = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        comb += 1
        if first + second == magic_num:
            print(f"Combination N: {comb}")
            print(f"({first} + {second} = {magic_num})")
            is_have_comb = True
    if is_have_comb:
        break

if not is_have_comb:
    print(f"{comb} combinations - neither equals {magic_num}")
