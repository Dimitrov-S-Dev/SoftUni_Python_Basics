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
