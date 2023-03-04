count = int(input())
hearthstone, game_f, overwatch, others = 0, 0, 0, 0

for _ in range(count):
    game = input()
    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        game_f += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

percent_heart =  (hearthstone / count) * 100
percent_f = (game_f / count) * 100
percent_over = (overwatch / count) * 100
percent_other = (others / count) * 100

print(f"Hearthstone - {percent_heart:.2f}%")
print(f"Fornite - {percent_f:.2f}%")
print(f"Overwatch - {percent_over:.2f}%")
print(f"Others - {percent_other:.2f}%")
