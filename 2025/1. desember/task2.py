
file = open("..\\Advent of code inputs\\2025\\2.txt")

password = 0
dial_pos = 50
for line in file:
    direction = line[0]
    ticks = int(line[1:])

    if direction == "R":
        for i in range(ticks):
            dial_pos += 1
            dial_pos = dial_pos % 100

            if dial_pos == 0:
                password += 1
            

    elif direction == "L":
        for i in range(ticks):
            dial_pos -= 1
            dial_pos = dial_pos % 100

            if dial_pos == 0:
                password += 1


    else:
        raise Exception(f"Not valid position: {dial_pos}")

print(f"Password is {password}")

file.close()