start = input()
end = input()

start_1 = int(start[0])
start_2 = int(start[1])
start_3 = int(start[2])
start_4 = int(start[3])
end_1 = int(end[0])
end_2 = int(end[1])
end_3 = int(end[2])
end_4 = int(end[3])



for a in range(start_1, end_1):
    if a % 2 == 0:
        continue
    for b in range(start_2, end_2 + 1):
        if b % 2 == 0:
            continue
        for c in range(start_3, end_3 + 1):
            if c % 2 == 0:
                continue
            for d in range(start_4, end_4 + 1):
                if d % 2 == 0:
                    continue
                print(f"{a}{b}{c}{d}", end=" ")