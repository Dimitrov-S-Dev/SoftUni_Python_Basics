# message = 0.6
# rose = 7.2
# key_holder = 3.6
# sketch = 18.2
# surprise = 22
#  hosting = 10 %

party_price = float(input())
message_count = int(input())
roses_count = int(input())
key_holders_count = int(input())
sketch_count = int(input())
surprises_count = int(input())

total = (message_count * 0.6) + (roses_count * 7.2) + (key_holders_count * 3.6) + \
        (sketch_count * 18.2) + (surprises_count * 22)

products_count = message_count + roses_count + key_holders_count\
                 + surprises_count + sketch_count

if products_count >= 25:
    total *= 0.65

final = total * 0.9
diff = abs(final - party_price)


if final >= party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
