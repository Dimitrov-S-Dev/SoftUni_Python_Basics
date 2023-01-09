sheet_price = float(input())
cover_price = float(input())
percent_discount = float(input())
designer_price = float(input())
percent_he_pay = float(input())

book_price = 899 * sheet_price + (2 * cover_price)
book_price *= (100 - percent_discount) / 100
book_price += designer_price
book_price *= (100 - percent_he_pay) / 100

print(f"Sancho should pay {book_price:.2f} BGN.")
