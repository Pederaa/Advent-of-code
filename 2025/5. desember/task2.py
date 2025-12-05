id_ranges = []
with open("2025\\5. desember\\input.txt") as file:
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        if line == "":
            break
    
        lower, upper = line.split("-")
        id_ranges.append([int(lower), int(upper)])

id_ranges.sort()
new_list = [id_ranges[0]]

for i in range(1, len(id_ranges)):
    if id_ranges[i][0] > new_list[-1][1]:
        new_list.append(id_ranges[i])
    
    elif id_ranges[i][1] >= new_list[-1][1]:
        new_list[-1][1] = id_ranges[i][1]
    
    else:
        continue

print(new_list)

total_fresh = 0
for j in range(len(new_list)):
    total_fresh += new_list[j][1] - new_list[j][0] + 1
    print(f"total fresh: {total_fresh}")

print(f"Svar: {total_fresh}")