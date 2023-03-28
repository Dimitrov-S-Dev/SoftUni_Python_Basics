capacity = float(input())
suitcases = 0
counter = 0
free_space = True
while True:
    counter += 1
    command = input()
    if command == "End":
        break
    volume = float(command)
    if counter % 3 == 0:
        volume *= 1.1
    if volume > capacity:
        free_space = False
        print(f"No more space!")
        break
    capacity -= volume
    suitcases += 1

if free_space:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases} suitcases loaded.")
