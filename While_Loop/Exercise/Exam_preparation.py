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
