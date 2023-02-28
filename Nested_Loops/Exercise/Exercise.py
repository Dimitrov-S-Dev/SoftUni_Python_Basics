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

# Task 4 Train the Trainers

jury_count = int(input())
command = input()
total_avr_present = 0
presentations_count = 0

while command != "Finish":
    presentation = command
    presentations_count += 1
    presentation_points = 0

    for points in range(jury_count):
        current_points = float(input())
        presentation_points += current_points

    avr_present_points = presentation_points / jury_count
    total_avr_present += avr_present_points

    print(f"{presentation}- {avr_present_points:.2f}")

    command = input()

total_aver = total_avr_present / presentations_count
print(f"Student's final assessment is {total_aver:.2f}")

# Task 5 Special Numbers

n = int(input())

for number in range(1111, 9999 + 1):
    is_special = True
    number_to_str = str(number)

    for num in number_to_str:
        if int(num) == 0 or n % int(num) != 0:
            is_special = False
            break
    if is_special:
        print(number_to_str, end=" ")

# Task 6 Cinema Tickets

command = input()
students = 0
standards = 0
kids = 0

while command != "Finish":
    movie_name = command
    free_places = int(input())
    ticket_type = input()
    current_taken_places = 0

    while ticket_type != "End":
        if ticket_type == "student":
            students += 1
        elif ticket_type == "standard":
            standards += 1
        elif ticket_type == "kid":
            kids += 1
        current_taken_places += 1
        if current_taken_places >= free_places:
            break
        ticket_type = input()
    percent_full = current_taken_places / free_places * 100
    print(f"{movie_name}-{percent_full:.2f}% full.")
    command = input()

total_tickets = students + standards + kids
percent_students = students / total_tickets * 100
percent_standards = standards / total_tickets * 100
percent_kids = kids / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student ticket.")
print(f"{percent_standards:.2f}% standard ticket.")
print(f"{percent_kids:.2f}% kids ticket.")
