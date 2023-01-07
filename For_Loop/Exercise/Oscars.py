actor_name = input()
starting_points = float(input())
number_of_jury = int(input())
actor_points = starting_points
got_nominee = False

for jury in range(number_of_jury):
    jury_name = input()
    current_points = float(input())
    actor_points += (current_points * len(jury_name) / 2)
    if actor_points >= 1250.5:
        print(f"Congratulations, {actor_name} got nominee for leading role with {actor_points}")
        got_nominee = True
        break

if not got_nominee:
    needed_points = 1250.5 - actor_points
    print(f"Sorry, {actor_name} you need {needed_points:.2f} more")
