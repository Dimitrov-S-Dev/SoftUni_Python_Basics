from math import floor

record_in_sec = float(input())
m_distance = float(input())
time_for_one_m = float(input())

time_in_sec = m_distance * time_for_one_m
time_delay_sec = floor(m_distance / 50) * 30
total_time = time_in_sec + time_delay_sec

diff = abs(total_time - record_in_sec)
if total_time >= record_in_sec:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
