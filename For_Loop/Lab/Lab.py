import sys
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

# Task 7 Sum of Numbers

n = int(input())
result = 0

for _ in range(n):
    current_num = int(input())
    result += current_num

print(result)

# Task 8 Set of Integers

max_num = -sys.maxsize
min_num = sys.maxsize

n = int(input())

for _ in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")

# Task 9 Left Right Sum

n = int(input())
left_part = 0

for left in range(n):
    current_num = int(input())
    left_part += current_num

right_part = 0

for right in range(n):
    current_num = int(input())
    right_part += current_num


if left_part == right_part:
    print(f"Yes, sum = {left_part}")
else:
    diff = abs(left_part - right_part)
    print(f"No, diff = {diff}")

# Task 10 Even Odd Sum

n = int(input())
even_sum = 0
odd_sum = 0

for num in range(1, n + 1):
    current_num = int(input())

    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No")
    print(f"Diff = {diff}")
    