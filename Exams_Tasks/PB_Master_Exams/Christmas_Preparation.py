paper_roll = int(input())
cloth_roll = int(input())
glue = float(input())
percent_discount = int(input())

price = (paper_roll * 5.8) + (cloth_roll * 7.2) + (glue * 1.2)
final_price = price * ((100 - percent_discount) / 100)

print(f"{final_price:.3f}")

