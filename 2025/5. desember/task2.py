def is_fresh(fresh_ranges, ing):
    for i in range(len(fresh_ranges)):
        if ing >= int(fresh_ranges[i][0]) and ing <= int(fresh_ranges[i][1]):
            return True

    return False

id_ranges = []
with open("2025\\5. desember\\input.txt") as file:
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        if line == "":
            break
    
        lower, upper = line.split("-")
        id_ranges.append((lower, upper))

max_value = 0
for i in range(len(id_ranges)):
    if int(id_ranges[i][1]) >= max_value:
        max_value = int(id_ranges[i][1])

total_fresh = 0
for j in range(max_value+1):
    if is_fresh(id_ranges, j):
        total_fresh += 1

print(f"max: {max_value}")
print(f"Svar: {total_fresh}")