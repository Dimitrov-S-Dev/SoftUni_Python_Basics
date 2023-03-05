a1 = int(input())
a2 = int(input())
n = int(input())

for symbol1 in range(a1, a2):
    if symbol1 % 2 == 0:
        continue
    for symbol2 in range(1, n):
        for symbol3 in range(1, n // 2):
            if (symbol3 + symbol2 + symbol1) % 2 != 0:
                print(f"{chr(symbol1)}-{symbol2}{symbol3}{symbol1}")
