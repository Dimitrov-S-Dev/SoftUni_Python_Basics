start = ord(input())
end = ord(input())
skip = ord(input())
comb = 0

for first in range(start, end + 1):
    if first == skip:
        continue

    for second in range(start, end + 1):
        if second == skip:
            continue

        for third in range(start, end + 1):
            if third == skip:
                continue
            comb += 1
            print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")

print(comb)
