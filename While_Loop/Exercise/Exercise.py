# Task 1 Old Library

searched_book = input()
command = input()
is_found = False
count = 0

while command != "No More Books":
    if command == searched_book:
        print(f"You checked {count} books and found it")
        is_found = True
        break
    count += 1
    command = input()


if not is_found:
    print(f"The book you search is not here")
    print(f"You checked {count} books.")

# Task 2 Exam Preparation

max_bad_marks = int(input())
task_name = input()
poor_grades = 0
grades = 0
is_excluded = False
tasks_count = 0
last_task = ""

while task_name != "Enough":
    last_task = task_name
    tasks_count += 1
    current_grade = int(input())
    if current_grade <= 4:
        poor_grades += 1
        if max_bad_marks == poor_grades:
            print(f"You need a break,{poor_grades} poor grades")
            is_excluded = True
            break
    grades += current_grade
    task_name = input()

avr_score = grades / tasks_count


if not is_excluded:
    print(f"Average score: {avr_score:.2f}")
    print(f"Number of problems: {tasks_count}")
    print(f"Last problem: {last_task}")

# Task 3 Vacation

needed_money = float(input())
money_in_hand = float(input())
spending_days = 0
days = 0
is_only_spending = False

while True:
    days += 1
    action = input()
    amount = float(input())
    if action == "save":
        spending_days = 0
        money_in_hand += amount
        if money_in_hand >= needed_money:
            break
    else:
        spending_days += 1
        if spending_days == 5:
            print(f"You cant save the money.")
            print(days)
            is_only_spending = True
            break


if not is_only_spending:
    print(f"You saved the money for {days} days.")

