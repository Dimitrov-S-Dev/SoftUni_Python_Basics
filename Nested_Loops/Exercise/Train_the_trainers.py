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
