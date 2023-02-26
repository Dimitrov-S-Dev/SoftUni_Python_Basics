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
