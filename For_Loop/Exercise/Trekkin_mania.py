number_of_groups = int(input())
musa_ala = 0
mon_bla = 0
kili_manjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(number_of_groups):
    current_people = int(input())
    if current_people <= 5:
        musa_ala += current_people
    elif current_people <= 12:
        mon_bla += current_people
    elif current_people <= 25:
        kili_manjaro += current_people
    elif current_people <= 40:
        k2 += current_people
    else:
        everest += current_people
    total_people += current_people


percent_musa_ala = musa_ala / total_people * 100
percent_mon_bla = mon_bla / total_people * 100
percent_kili_manjaro = kili_manjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musa_ala:.2f}%")
print(f"{percent_mon_bla:.2f}%")
print(f"{percent_kili_manjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
