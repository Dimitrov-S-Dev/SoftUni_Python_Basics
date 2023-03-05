movie_budget = float(input())
actors_num = int(input())
actors_cloths = float(input())

decor_price = movie_budget * 0.1
cloth_sum = actors_cloths * actors_num

if actors_num > 150:
    cloth_sum *= 0.9

total = decor_price + cloth_sum
diff = abs(total - movie_budget)

if total > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
