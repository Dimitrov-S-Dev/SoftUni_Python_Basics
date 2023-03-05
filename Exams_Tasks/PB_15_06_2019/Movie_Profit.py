movie_name = input()
days = int(input())
profit = 0

tickets_sold = int(input())
ticket_price = float(input())
percent = 1 - int(input()) / 100
profit += ticket_price * tickets_sold * percent * days

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
