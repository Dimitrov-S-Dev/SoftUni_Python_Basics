#  Task 1 Pyramid of Numbers

number = int(input())
counter = 1
is_all_printed = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            is_all_printed = True
            break
    if is_all_printed:
        break
    print()

# Task 2 Equal Sum on Odd/Even Positions

first = int(input())
second = int(input())

for number in range(first, second + 1):
    odd_sum = 0
    even_sum = 0
    num_to_str = str(number)

    for index,value in enumerate(num_to_str):
        if index % 2 == 0:
            odd_sum += int(value)
        else:
            even_sum += int(value)
    if odd_sum == even_sum:
        print(num_to_str, end=" ")

# Task 3 Sum Prime Non Prime Numbers

command = input()
prime_num_sum = 0
non_prime_sum = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print(f"Number is negative")
    else:
        is_prime = True
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_num_sum += number
        else:
            non_prime_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_num_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")




