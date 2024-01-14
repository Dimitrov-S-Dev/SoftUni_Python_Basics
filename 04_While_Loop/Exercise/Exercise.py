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
last_task = ""
bad_marks = 0
score = 0
task_num = 0
flag = False

while task_name != "Enough":
    last_task = task_name
    curr_mark = int(input())
    score += curr_mark
    task_num += 1
    if curr_mark <= 4:
        bad_marks += 1
    if bad_marks == max_bad_marks:
        flag = True
        break
    task_name = input()

if last_task:
    avg = score / task_num
    if flag:
        print(f"You need a break, {bad_marks} poor grades.")
    else:
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {task_num}")
        print(f"Last problem: {last_task}")

# Task 3 Vacation

needed_money = float(input())
money_in_hand = float(input())
spending_count = 0
days_count = 0

while True:
    days_count += 1
    command = input()
    curr_money = float(input())
    if command == "save":
        spending_count = 0
        money_in_hand += curr_money
    else:
        spending_count += 1
        money_in_hand = max(money_in_hand - curr_money, 0)
    if spending_count == 5:
        print(f"You can't save the money.")
        print(f"{days_count}")
        break

    if money_in_hand >= needed_money:
        print(f"You saved the money for {days_count} days.")
        break

# Task 4 Steps

target = 10_000
steps_walked = 0

while steps_walked < target:
    command = input()
    if command == "Going home":
        current_steps = int(input())
        steps_walked += current_steps
        break
    else:
        current_steps = int(command)
        steps_walked += current_steps


diff = abs(target - steps_walked)
if steps_walked >= target:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

# Task 5 Coins

money = float(input())
coins = int(money * 100)
coins_count = 0

while coins:
    if coins >= 200:
        coins_count += coins // 200
        coins = coins % 200
    elif coins >= 100:
        coins_count += coins // 100
        coins = coins % 100
    elif coins >= 50:
        coins_count += coins // 50
        coins = coins % 50
    elif coins >= 20:
        coins_count += coins // 20
        coins = coins % 20
    elif coins >= 10:
        coins_count += coins // 10
        coins = coins % 10
    elif coins >= 5:
        coins_count += coins // 5
        coins = coins % 5
    elif coins >= 2:
        coins_count += coins // 2
        coins = coins % 2
    elif coins >= 1:
        coins_count += coins // 1
        coins = coins % 1

print(int(coins_count))

# Task 6 Birthday Cake

cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_length * cake_width

command = input()
is_cake_over = False

while command != "STOP":
    current_piece = int(command)
    cake_pieces -= current_piece
    if cake_pieces < 0:
        is_cake_over = True
        break
    command = input()


if is_cake_over:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more")
else:
    print(f"{cake_pieces} pieces are left.")

# Task 7 Moving

space_width = int(input())
space_length = int(input())
space_height = int(input())
space_volume = space_height * space_length * space_width

command = input()
is_have_space = True

while command != "Done":
    current_box = int(command)
    space_volume -= current_box
    if space_volume < 0:
        is_have_space = False
        break
    command = input()

if is_have_space:
    print(f"{space_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_volume)} Cubic meters more.")
