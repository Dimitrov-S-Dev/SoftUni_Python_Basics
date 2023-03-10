eggs = int(input())
is_over = False
eggs_sold = 0

while True:
    command = input()
    if command == "Close":
        break
    count = int(input())
    if command == "Fill":
        eggs += count
    elif command == "Buy":
        if eggs < count:
            is_over = True
            break
        else:
            eggs -= count
            eggs_sold += count

if is_over:
    print(f"Not enough eggs in store!")
    print(f"You can buy only {eggs}.")
else:
    print(f"Store is closed!")
    print(f"{eggs_sold} eggs sold.")
