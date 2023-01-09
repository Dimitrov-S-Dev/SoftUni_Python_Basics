t_shirt_price = float(input())
target_amount = float(input())
is_ball_won = False

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes = (t_shirt_price + shorts_price) * 2

total = (t_shirt_price + shorts_price + socks_price + shoes) * 0.85

if total >= target_amount:
    is_ball_won = True

if is_ball_won:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total} lv.")
else:
    print(f"No, he will not earn the replica ball")
    print(f"He needs {target_amount - total:.2f} lv.")

