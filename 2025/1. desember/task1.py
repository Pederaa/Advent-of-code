
file = open("..\\Advent of code inputs\\2025\\1.txt")

password = 0
dial_pos = 50
for line in file:
    direction = line[0]
    ticks = int(line[1:])

    if direction == "R":
        dial_pos += ticks
            

    elif direction == "L":
        dial_pos -= ticks

    else:
        raise Exception(f"Not valid position: {dial_pos}")

    dial_pos = dial_pos%100

    if dial_pos == 0:
        password += 1

print(f"Password is {password}")

file.close()