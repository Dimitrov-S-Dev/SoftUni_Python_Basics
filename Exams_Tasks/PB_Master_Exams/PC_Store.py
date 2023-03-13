dollar = 1.57
# price in dollars
processor = float(input())
video_cart = float(input())
one_ram = float(input())
ram_count = int(input())
percent_discount = float(input())

total = (processor + video_cart) * dollar * (1 - percent_discount)
total += ram_count * one_ram * dollar

print(f"Money needed - {total:.2f} lv.")
