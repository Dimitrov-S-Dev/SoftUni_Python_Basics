start = int(input())
end = int(input())

for first in range(start, end + 1):
    for second in range(start, end + 1):
        for third in range(start, end + 1):
            for forth in range(start, end + 1):
                if forth > first:
                    continue
                if (second + third) % 2 != 0:
                    continue
                if (first % 2 == 0 and forth % 2 != 0) or (first % 2 != 0 and forth % 2 == 0):

                    print(f"{first}{second}{third}{forth}", end=" ")
