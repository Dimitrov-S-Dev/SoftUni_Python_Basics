days = int(input())
liters = 0
degrees = 0

for _ in range(days):
    current_liter = float(input())
    current_degrees = float(input())
    liters += current_liter
    degrees += current_degrees * current_liter

final_degrees = degrees / liters

print(f"Liter: {liters:.2f}")
print(f"Degrees: {final_degrees:.2f}")

if final_degrees < 38:
    print(f"Not good, you should baking!")
elif final_degrees <= 42:
    print(f"Super!")
else:
    print("Dilution with distilled water!")
