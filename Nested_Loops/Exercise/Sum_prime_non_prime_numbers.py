command = input()
prime_num_sum = 0
non_prime_sum = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print(f"Number is negative")
    else:
        is_prime = True
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_num_sum += number
        else:
            non_prime_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_num_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
