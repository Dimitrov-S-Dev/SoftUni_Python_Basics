time = int(input())
scenes = int(input())
one_scene_time = int(input())

preparation_time = time * 0.15
recording_time = (scenes * one_scene_time) + preparation_time

diff = round(abs(time - recording_time))
if recording_time > time:
    print(f"Time is up! To complete the movie you need {diff} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
