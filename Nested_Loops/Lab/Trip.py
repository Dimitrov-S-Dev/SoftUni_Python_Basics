while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    while budget >= 0:
        saving = float(input())
        budget -= saving
    print(f"Going to {destination}")
