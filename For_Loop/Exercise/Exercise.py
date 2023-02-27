# Task 1 Numbers to 1000 Ending on 7

for number in range(1001):
    if number % 10 == 7:
        print(number)

# Task 2 Element Equal to Sum of Rest

import sys

n = int(input())
max_num = -sys.maxsize
sum_of_numbers = 0

for _ in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_of_numbers += current_num


if max_num == sum_of_numbers - max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    diffr = abs(max_num - (sum_of_numbers - max_num))
    print("No")
    print(f"Diff = {diffr}")

# Task 3 Histogram

n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(n):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    else:
        p5 += 1

percent_p1 = p1 / n * 100
percent_p2 = p2 / n * 100
percent_p3 = p3 / n * 100
percent_p4 = p4 / n * 100
percent_p5 = p5 / n * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")