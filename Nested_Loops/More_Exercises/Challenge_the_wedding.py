mens = int(input())
women = int(input())
tables = int(input())

is_finish = False

for m in range(1, mens + 1):
    for w in range(1, women + 1):
        tables -= 1
        print(f"({m}<->{w})", end=" ")
        if tables == 0:
            is_finish = True
            break
    if is_finish:
        break
