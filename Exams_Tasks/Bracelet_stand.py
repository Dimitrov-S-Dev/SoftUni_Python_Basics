pocket_money_per_day = float(input())
sales_per_day = float(input())
outcome = float(input())
gift_price = float(input())

total_money = ((sales_per_day + pocket_money_per_day) * 5) - outcome

if total_money >= gift_price:
    print(f"{total_money:.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - total_money
    print(f"Insufficient money: {diff:.2f} BGN.")
