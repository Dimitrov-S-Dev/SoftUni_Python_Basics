start = ord("A")
end = ord(input())
number_of_rows = int(input())
seats_ = int(input())
seats = seats_

for letter in range(start, end + 1):
    for rows in range(1, number_of_rows + 1):
        if rows % 2 == 0:
            seats *= 2
        else:
            seats = seats_
        for seat in range(97, (97 + seats)):
            print(f"{chr(letter)}{rows}{(chr(seat))}")

    number_of_rows += 1
