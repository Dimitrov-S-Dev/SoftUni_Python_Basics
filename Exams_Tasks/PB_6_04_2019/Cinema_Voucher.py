voucher = int(input())
tickets_bought = 0
products_bought = 0

while True:
    condition = False
    command = input()
    if command == "End":
        break
    if len(command) > 8:
        sum_numbers = ord(command[0]) + ord(command[1])
        if sum_numbers <= voucher:
            voucher -= sum_numbers
            tickets_bought += 1
        else:
            condition = True
    else:
        if len(command) <= 8:
            sum_numbers = ord(command[0])
            if sum_numbers <= voucher:
                voucher -= sum_numbers
                products_bought += 1
            else:
                condition = True
    if condition:
        break

print(f"{tickets_bought}")
print(f"{products_bought}")
