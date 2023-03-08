height = int(input())
start_point = height - 30
attempts = 0

while True:
    has_success = False
    current_height = 0
    failed_height = 0
    for _ in range(3):
        current_attempt = int(input())
        attempts += 1
        failed_height = current_attempt
        if current_attempt > start_point:
            start_point += 5
            has_success = True
            current_height = current_attempt
            break
    if has_success and start_point > height:
        print(f"Tihomir succeeded, he jumped over {height}cm after {attempts} jumps.")
        break
    elif not has_success:
        print(f"Tihomir failed at {failed_height}cm after {attempts} jumps.")
        break
    continue
