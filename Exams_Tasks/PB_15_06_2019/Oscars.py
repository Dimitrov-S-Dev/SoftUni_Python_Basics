actor_name = input()
points = float(input())
judges = int(input())
won_oscar = False

for _ in range(judges):
    judge_name = input()
    curr_points = float(input())
    points += (len(judge_name) * curr_points) / 2
    if points > 1250.5:
        won_oscar = True
        break

if won_oscar:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    diff = 1250.5 - points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
