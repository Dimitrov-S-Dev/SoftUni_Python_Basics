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
