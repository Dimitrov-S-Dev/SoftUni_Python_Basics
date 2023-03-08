yearly_tax = float(input())

shoes_price = yearly_tax * 0.6
clothes = shoes_price * 0.8
ball_price = clothes / 4
accessories_price = ball_price / 5

total = yearly_tax + shoes_price + clothes
total += ball_price + accessories_price

print(f"{total:.2f}")
