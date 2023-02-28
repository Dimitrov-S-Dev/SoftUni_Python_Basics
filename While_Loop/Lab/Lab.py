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

