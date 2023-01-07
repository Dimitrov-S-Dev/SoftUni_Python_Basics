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
