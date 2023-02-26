open_browsers = int(input())
salary = int(input())


for _ in range(open_browsers):
    current_browser = input()
    if current_browser == "Facebook":
        salary -= 150
    elif current_browser == "Instagram":
        salary -= 100
    elif current_browser == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary")
        break

print(f"{salary:.2f}")
