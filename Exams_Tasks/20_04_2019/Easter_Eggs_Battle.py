f_player_eggs = int(input())
s_player_eggs = int(input())
is_finish = False

while True:
    command = input()
    if command == "End":
        break
    if command == "one":
        s_player_eggs -= 1
    elif command == "two":
        f_player_eggs -= 1
    if f_player_eggs == 0 or s_player_eggs == 0:
        is_finish = True
        break

if is_finish:
    if f_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {s_player_eggs} eggs left.")
    else:
        print(f"Player two is out of eggs. Player one has {f_player_eggs} eggs left.")
else:
    print(f"Player one has {f_player_eggs} eggs left.")
    print(f"Player two has {s_player_eggs} eggs left.")
