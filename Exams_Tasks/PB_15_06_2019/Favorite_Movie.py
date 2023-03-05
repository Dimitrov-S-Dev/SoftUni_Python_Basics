favorite_movie = ""
favorite_movie_points = 0
limit_reached = False
count = 0

while True:
    current_points = 0
    command = input()
    if command == "STOP":
        break
    movie_name = command
    for char in movie_name:
        current_points += ord(char)
    for char in movie_name:
        if char.islower():
            current_points -= 2 * len(movie_name)
        elif char.isupper():
            current_points -= len(movie_name)
        else:
            continue
    if current_points > favorite_movie_points:
        favorite_movie_points = current_points
        favorite_movie = movie_name
    count += 1
    if count == 7:
        limit_reached = True
        break

if limit_reached:
    print(f"The limit is reached.")
print(f"The best movie for you is {favorite_movie} with {favorite_movie_points} ASCII sum.")
