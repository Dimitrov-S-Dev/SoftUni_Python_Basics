country = input()
discipline = input()
difficult = 0
perform = 0

if country == "Russia":
    if discipline == "ribbon":
        difficult = 9.100
        perform = 9.400
    elif discipline == "hoop":
        difficult = 9.300
        perform = 9.800
    elif discipline == "rope":
        difficult = 9.600
        perform = 9.000
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficult = 9.600
        perform = 9.400
    elif discipline == "hoop":
        difficult = 9.550
        perform = 9.750
    elif discipline == "rope":
        difficult = 9.500
        perform = 9.400
elif country == "Italy":
    if discipline == "ribbon":
        difficult = 9.200
        perform = 9.500
    elif discipline == "hoop":
        difficult = 9.450
        perform = 9.350
    elif discipline == "rope":
        difficult = 9.700
        perform = 9.150

total = difficult + perform
p_to_max = ((20 - total) / 20) * 100

print(f"The team of {country} get {total:.3f} on {discipline}.")
print(f"{p_to_max:.2f}%")
