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

