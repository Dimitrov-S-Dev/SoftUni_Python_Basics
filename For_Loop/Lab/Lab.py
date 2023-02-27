# Task 1 Numbers from 1 to 100

for num in range(1, 100):
    print(num)

# Task 2 Numbers from 1 to N with step 3
n = int(input())
for number in range(1, n + 1, 3):
    print(number)

# Task 3 Even Squares of Number 2

n = int(input())
for number in range(n + 1):
    if number % 2 == 0:
        print(f"{2**number}")

# Task 4 Numbers from N to 1

n = int(input())
for number in range(n, 0, - 1):
    print(number)

# Task 5 Symbols

text = input()
for char in text:
    print(char)

# Task 6 Sum of Vows

a, e, i, o, u = 1, 2, 3, 4, 5
text = input()
result = 0

for char in text:
    if char == 'a':
        result += 1
    elif char == 'e':
        result += 2
    elif char == 'i':
        result += 3
    elif char == 'o':
        result += 4
    elif char == 'u':
        result += 5

print(result)

# Task 7 