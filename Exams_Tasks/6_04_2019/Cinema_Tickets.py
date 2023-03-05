student_t = 0
standard_t = 0
kid_t = 0

while True:
    movie_full = 0
    command = input()
    if command == "Finish":
        break
    movie_name = command
    free_places = int(input())
    ticket = input()
    current_p = 0
    while ticket != "End":
        if ticket == "student":
            student_t += 1
        elif ticket == "standard":
            standard_t += 1
        elif ticket == "kid":
            kid_t += 1
        current_p += 1
        if current_p == free_places:
            break
        ticket = input()
    movie_full += current_p
    percen_full = (movie_full / free_places) * 100
    print(f"{movie_name} - {percen_full:.2f}% full.")

total_t = student_t + standard_t + kid_t
print(f"Total tickets: {total_t}")
percent_stud = (student_t / total_t) * 100
percent_stand = (standard_t / total_t) * 100
percent_kid = (kid_t / total_t) * 100
print(f"{percent_stud:.2f}% student tickets.")
print(f"{percent_stand:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
