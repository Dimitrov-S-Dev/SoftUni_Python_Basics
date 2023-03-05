import sys
movies_count = int(input())
max_rating = 0
max_r_movie = -sys.maxsize
min_rating = sys.maxsize
min_r_movie = ""
total_rating = 0

for _ in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_r_movie = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        min_r_movie = movie_name
    total_rating += movie_rating

print(f"{max_r_movie} is with highest rating: {max_rating}")
print(f"{min_r_movie} is with lowest rating: {min_rating}")
avg_rating = total_rating / movies_count
print(f"Average rating: {avg_rating:.1f}")
