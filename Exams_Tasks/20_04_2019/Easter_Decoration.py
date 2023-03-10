clients = int(input())
total = 0

for _ in range(clients):
    curr_total = 0
    product_count = 0
    while True:
        command = input()
        if command == "Finish":
            break
        product = command
        if product == "basket":
            curr_total += 1.5
        elif product == "wreath":
            curr_total += 3.8
        elif product == "chocolate bunny":
            curr_total += 7
        product_count += 1
    if product_count % 2 == 0:
        curr_total *= 0.8
    total += curr_total
    print(f"You purchased {product_count} items for {curr_total:.2f} leva.")

avg_bill = total / clients
print(f"Average bill per client is: {avg_bill:.2f} leva.")
