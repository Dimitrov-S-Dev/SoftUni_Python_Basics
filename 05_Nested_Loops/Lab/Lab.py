# Task 1 Clock

for hours in range(24):
    for minutes in range(60):
        print(f"{hours}:{minutes}")

# Task 2 Multiplication Table

for first in range(1, 11):
    for second in range(1, 11):
        total = first * second
        print(f"{first} * {second} = {total}")

# Task 3 Combinations

n = int(input())
count = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            if x1 + x2 + x3 == n:
                count += 1

print(count)

# Task 4 Sum of Two Digits

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

# Task 5 Trip

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())

    while budget > 0:
        savings = float(input())
        budget -= savings
    print(f"Going to {destination}")

# Task 6 Building

floor_count = int(input())
room_count = int(input())

for floor in range(floor_count, 0, -1):
    result = ""
    for room in range(room_count):
        if floor == floor_count:
            letter = "L"
        elif floor % 2 == 0:
            letter = "O"
        else:
            letter = "A"
        result += f"{letter}{floor}{room} "
    print(result.strip())
