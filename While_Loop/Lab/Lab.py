import sys
# Task 1 Words Reading

command = input()

while command != "Stop":
    print(command)
    command = input()

# Task 2 Password

name = input()
password = input()
command = input()

while command != password:
    command = input()

print(f"Welcome {name}!")

# Task 3 Sum of Numbers

n = int(input())
sum_numbers = 0

while sum_numbers < n:
    number = int(input())
    sum_numbers += number

print(n)

# Task 4 Numbers 2K + 1

n = int(input())
count = 1

while count <= n:
    print(count)
    count = (count * 2) + 1

# Task 5 Balance Amount

command = input()
amount = 0

while command != "NoMoreMoney":
    current_amount = float(command)
    if current_amount < 0:
        print(f"Invalid operation!")
        break
    else:
        amount += current_amount
        print(f"Increase: {current_amount}")
    command = input()


print(f"{amount:.2f}")

# Task 6 Biggest Number

command = input()
max_num = 0

while command != "Stop":
    current_num = int(command)
    if current_num > max_num:
        max_num = current_num
    command = input()

print(max_num)

# Task 7 Smallest Number

command = input()
min_num = sys.maxsize

while command != "Stop":
    current_num = int(command)
    if current_num < min_num:
        min_num = current_num
    command = input()

print(min_num)


# Task 8 Graduation

student_name = input()
fails = 0
grade = 1
total_grades = 0
is_excluded = False

while grade < 13:
    year_grade = float(input())
    if year_grade < 4:
        fails += 1
        if fails == 2:
            print(f"{student_name} has been excluded at {grade} grade")
            is_excluded = True
            break
    else:
        grade += 1
        total_grades += year_grade


aver_grade = total_grades / 12
if not is_excluded:
    print(f"{student_name} graduated.Average grade: {aver_grade:.2f}")
