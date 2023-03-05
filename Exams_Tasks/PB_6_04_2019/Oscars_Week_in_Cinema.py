movie_name = input()
hall = input()
number_of_tickets = int(input())
price = 0

if movie_name == "A Star Is Born":
    if hall == "normal":
        price = 7.5
    elif hall == "luxury":
        price = 10.5
    elif hall == "ultra luxury":
        price = 13.5
elif movie_name == "Bohemian Rhapsody":
    if hall == "normal":
        price = 7.35
    elif hall == "luxury":
        price = 9.45
    elif hall == "ultra luxury":
        price = 12.75
elif movie_name == "Green Book":
    if hall == "normal":
        price = 8.15
    elif hall == "luxury":
        price = 10.25
    elif hall == "ultra luxury":
        price = 13.25
elif movie_name == "The Favourite":
    if hall == "normal":
        price = 8.75
    elif hall == "luxury":
        price = 11.55
    elif hall == "ultra luxury":
        price = 13.95

total = price * number_of_tickets
print(f"{movie_name} -> {total:.2f} lv.")