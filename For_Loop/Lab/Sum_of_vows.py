a, e, i, o, u = 1, 2, 3, 4, 5

text = input()
result = 0

for char in text:
    if char == 'a':
        result += 1
    elif char == 'e':
        result += 2
    elif char == 'i':
        result += 3
    elif char == 'o':
        result += 4
    elif char == 'u':
        result += 5


print(result)
