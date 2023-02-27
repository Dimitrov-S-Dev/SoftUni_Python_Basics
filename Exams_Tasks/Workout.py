from math import ceil

training_days = int(input())
first_day_run_km = float(input())
final_run = first_day_run_km

for days in range(1, training_days + 1):
    percent_increase = int(input()) / 100
    current_run = first_day_run_km * percent_increase
    first_day_run_km += current_run
    final_run += first_day_run_km

diff = ceil(abs(1000 - final_run))

if final_run >= 1000:
    print(f"You have done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers.")
