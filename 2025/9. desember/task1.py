with open("2025\\9. desember\\input.txt") as file:
    contents = file.readlines()

max_area = 0
for i in range(len(contents)-1):
    for j in range(i, len(contents)):
        c1 = contents[i].split(",")
        c2 = contents[j].split(",")

        area = (abs(int(c1[0]) - int(c2[0]) + 1))*(abs(int(c1[1]) - int(c2[1]) + 1))

        max_area = max(max_area, area)


print(f"Svar: {max_area}")