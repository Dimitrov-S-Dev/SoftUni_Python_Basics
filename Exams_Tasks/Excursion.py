people_in_group = int(input())
nights = int(input())
transport = int(input())
museum = int(input())

total_group = ((nights * 20) + (transport * 1.6) + (museum * 6)) * people_in_group
final = total_group * 1.25

print(f"{final:.2f}")
