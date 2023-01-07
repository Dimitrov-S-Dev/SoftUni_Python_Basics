command = input()
students = 0
standards = 0
kids = 0

while command != "Finish":
    movie_name = command
    free_places = int(input())
    ticket_type = input()
    current_taken_places = 0
    while ticket_type != "End":
        if ticket_type == "student":
            students += 1
        elif ticket_type == "standard":
            standards += 1
        elif ticket_type == "kid":
            kids += 1
        current_taken_places += 1
        if current_taken_places >= free_places:
            break
        ticket_type = input()
    percent_full = current_taken_places / free_places * 100
    print(f"{movie_name}-{percent_full:.2f}% full.")
    command = input()

total_tickets = students + standards + kids
percent_students = students / total_tickets * 100
percent_standards = standards / total_tickets * 100
percent_kids = kids / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student ticket.")
print(f"{percent_standards:.2f}% standard ticket.")
print(f"{percent_kids:.2f}% kids ticket.")
