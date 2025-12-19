

if __name__ == "__main__":
    with open("..\\Advent of code inputs\\2025\\9.txt") as file:
        contents = file.readlines()

    corners = []
    for i in range(len(contents)):
        x, y = contents[i].split(",")
        corners.append((x, y))