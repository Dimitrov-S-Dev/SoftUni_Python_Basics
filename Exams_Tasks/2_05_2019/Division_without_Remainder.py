count = int(input())
p2 = 0 # divisible on 2
p3 = 0 # divisible on 3
p4 = 0 # divisible on 4

for _ in range(count):
    curr_num = int(input())
    if curr_num % 2 == 0:
        p2 += 1
    if curr_num % 3 == 0:
        p3 += 1
    if curr_num % 4 == 0:
        p4 += 1


percent_p2 = (p2 / count) * 100
percent_p3 = (p3 / count) * 100
percent_p4 = (p4 / count) * 100

print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
