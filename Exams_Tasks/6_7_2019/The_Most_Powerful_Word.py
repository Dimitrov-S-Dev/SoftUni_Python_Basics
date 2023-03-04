max_points = 0
max_word = ""

while True:
    points = 0
    command = input()
    words = "aeiouy"
    condition = False
    if command == "End of words":
        break
    for char in command:
        points += ord(char)
    for el in words:
        if el == command[0].lower():
            condition = True
            break
    if condition:
        points *= len(command)
    else:
        points //= len(command)
    if points > max_points:
        max_points = points
        max_word = command

print(f"The most powerful word is {max_word} - {max_points}")

