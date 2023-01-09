ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
avr_astronaut_height = float(input()) + 0.4

ship_volume = ship_width * ship_length * ship_height
room_volume = 2 * 2 * avr_astronaut_height

astronauts_count = int(ship_volume / room_volume)

if 3 <= astronauts_count <= 10:
    print(f"The spacecraft holds {astronauts_count} astronauts.")
elif astronauts_count < 3:
    print(f"The spacecraft is too small")
else:
    print(f"The spacecraft is too big.")
