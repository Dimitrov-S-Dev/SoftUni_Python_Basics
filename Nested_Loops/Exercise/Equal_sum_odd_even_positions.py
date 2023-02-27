first = int(input())
second = int(input())

for number in range(first, second + 1):
    odd_sum = 0
    even_sum = 0
    num_to_str = str(number)

    for index,value in enumerate(num_to_str):
        if index % 2 == 0:
            odd_sum += int(value)
        else:
            even_sum += int(value)
    if odd_sum == even_sum:
        print(num_to_str, end=" ")
