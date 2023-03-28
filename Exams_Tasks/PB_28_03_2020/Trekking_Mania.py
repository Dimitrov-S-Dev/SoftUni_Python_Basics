musala, monblan, kilimanjaro, k2, everest = 0, 0, 0, 0, 0

number_of_groups = int(input())

for _ in range(number_of_groups):
    people = int(input())
    if people <= 5:
        musala += people
    elif people <= 12:
        monblan += people
    elif people <= 25:
        kilimanjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

total = musala + monblan + kilimanjaro + k2 + everest

p_musala = (musala / total) * 100
p_monblan = (monblan / total) * 100
p_kilimanjaro = (kilimanjaro / total) * 100
p_k2 = (k2 / total) * 100
p_everest = (everest / total) * 100

print(f"{p_musala:.2f}%")
print(f"{p_monblan:.2f}%")
print(f"{p_kilimanjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")
