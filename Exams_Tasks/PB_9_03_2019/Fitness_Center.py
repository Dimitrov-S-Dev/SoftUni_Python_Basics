visitors = int(input())
back, chest, legs, abs, protein_shake, protein_bar, protein, work_out = 0, 0, 0, 0, 0, 0, 0, 0

for _ in range(visitors):
    c_input = input()
    if c_input == "Back":
        back += 1
        work_out += 1
    elif c_input == "Chest":
        chest += 1
        work_out += 1
    elif c_input == "Legs":
        legs += 1
        work_out += 1
    elif c_input == "Abs":
        abs += 1
        work_out += 1
    elif c_input == "Protein shake":
        protein_shake += 1
        protein += 1
    elif c_input == "Protein bar":
        protein_bar += 1
        protein += 1

p_work_out = (work_out / visitors) * 100
p_protein = (protein / visitors) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{p_work_out:.2f}% - work out")
print(f"{p_protein:.2f}% - protein")
