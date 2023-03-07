first_player = input()
second_player = input()
fp_points = 0
sp_points = 0
num_wars = 0
is_winner = False
winner = ""

while True:
    command = input()
    if command == "End of game":
        break
    fp_card = int(command)
    sp_card = int(input())
    if fp_card == sp_card:
        print("Number wars!")
        num_wars += 1
        continue
    if num_wars == 1:
        is_winner = True
        if fp_card > sp_card:
            winner = first_player
        else:
            winner = second_player
        break
    elif fp_card > sp_card:
        fp_points += fp_card - sp_card
    else:
        sp_points += sp_card - fp_card


if is_winner:
    if winner == first_player:
        print(f"{first_player} is winner with {fp_points} points")
    else:
        print(f"{second_player} is winner with {sp_points} points")
else:
    print(f"{first_player} has {fp_points} points")
    print(f"{second_player} has {sp_points} points")
