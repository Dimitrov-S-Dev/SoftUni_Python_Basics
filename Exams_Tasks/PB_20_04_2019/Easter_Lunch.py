easter_cakes = int(input())
eggs= int(input())
cookies = int(input())

e_cake_price = easter_cakes * 3.2
egg_price = eggs * 4.35
cookie_price = cookies * 5.4
paint_price = eggs * 12 * 0.15

total = e_cake_price + egg_price + cookie_price + paint_price

print(f"{total:.2f}")
