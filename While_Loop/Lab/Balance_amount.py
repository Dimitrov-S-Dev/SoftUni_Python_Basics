command = input()
amount = 0

while command != "NoMoreMoney":
    current_amount = float(command)
    if current_amount < 0:
        print(f"Invalid operation!")
        break
    else:
        amount += current_amount
        print(f"Increase: {current_amount}")
    command = input()


print(f"{amount:.2f}")
