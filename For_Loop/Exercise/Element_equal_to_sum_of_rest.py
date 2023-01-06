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
