n = int(input())

for number in range(1111, 9999 + 1):
    is_special = True
    number_to_str = str(number)
    for num in number_to_str:
        if int(num) == 0 or n % int(num) != 0:
            is_special = False
            break
    if is_special:
        print(number_to_str, end=" ")
