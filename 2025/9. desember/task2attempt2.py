

if __name__ == "__main__":
    with open("2025\\9. desember\\input.txt") as file:
        contents = file.readlines()

    corners = []
    for i in range(len(contents)):
        x, y = contents[i].split(",")
        corners.append((x, y))