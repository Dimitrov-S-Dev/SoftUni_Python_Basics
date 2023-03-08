from math import ceil,floor

one_racket_price = float(input())
racket_count = int(input())
shoes_count = int(input())

racket_total = one_racket_price * racket_count
shoes_price = one_racket_price / 6
shoes_total = shoes_price * shoes_count

total = racket_total + shoes_total
eq_total = total * 0.2
total += eq_total

dj_part = total / 8
sp_part = total * (7/8)

print(f"Price to be paid by Djokovic {floor(dj_part)}")
print(f"Price to be paid by sponsors {ceil(sp_part)}")
