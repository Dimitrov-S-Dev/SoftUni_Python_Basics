n = int(input())
m = int(input())
s = int(input())

for address in range(m, n - 1, - 1):
    if address % 2 != 0 or address % 3 != 0:
        continue
    if address == s:
        break
    print(f"{address}", end=" ")
