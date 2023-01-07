searched_book = input()
command = input()
is_found = False
count = 0

while command != "No More Books":
    if command == searched_book:
        print(f"You checked {count} books and found it")
        is_found = True
        break
    count += 1
    command = input()

if not is_found:
    print(f"The book you search is not here")
    print(f"You checked {count} books.")
