with open("2025\\5. desember\\input.txt") as file:
    id_ranges = []
    fresh_count = 0
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        if line == "":
            continue

        try:
            lower, upper = line.split("-")
            id_ranges.append((lower, upper))
        
        except ValueError:
            for i in range(len(id_ranges)):
                if int(line) >= int(id_ranges[i][0]) and int(line) <= int(id_ranges[i][1]):
                    fresh_count += 1
                    print(f"{id_ranges[i][0]} <= {line} <= {id_ranges[i][1]}")

                    break
    

    print(f"Svar: {fresh_count}")


        
