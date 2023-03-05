from math import ceil

serial_name = input()
seasons = int(input())
episodes = int(input())
time = float(input())

episode_commercials = time * 0.2
episode_time = time + episode_commercials
additional_time = seasons * 10

total_time = (episode_time * episodes * seasons) + additional_time

print(f"Total time needed to watch the {serial_name} series is {ceil(total_time)} minutes.")
