minutes = int(input())
seconds = int(input())
distance_m = float(input())
sec_for_100 = int(input())

control_in_sec = minutes * 60 + seconds
time_delay = distance_m / 120
total_time_delay = time_delay * 2.5

time = (distance_m / 100) * sec_for_100 - total_time_delay

if time <= control_in_sec:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    diff = time - control_in_sec
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
