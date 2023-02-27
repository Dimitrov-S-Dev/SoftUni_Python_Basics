import sys
command = input()
min_num = sys.maxsize

while command != "Stop":
    current_num = int(command)
    if current_num < min_num:
        min_num = current_num
    command = input()

print(min_num)
