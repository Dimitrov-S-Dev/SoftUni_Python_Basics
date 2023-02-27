first = int(input())
second = int(input())
first_end = first + int(input())
second_end = second + int(input())

for a in range(first, first_end + 1):
    is_prime_a = True

    for prime_a in range(2, a):
        if a % prime_a == 0:
            is_prime_a = False
            break
    if not is_prime_a:
        continue

    for b in range(second, second_end + 1):
        is_prime_b = True
        for prime_b in range(2, b):
            if b % prime_b == 0:
                is_prime_b = False
                break
        if not is_prime_b:
            continue
        print(f"{a}{b}")
