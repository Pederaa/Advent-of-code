

with open("..\\Advent of code inputs\\2025\\3.txt") as file:
    total = 0
    k_values = list(range(0, 9+1))
    k_values.reverse()

    for line in file:
        
        if line[-1] == '\n':
            line = line[:-1]

        li = list(line)[:int(len(line)-1)]

        first_index = ''
        second_index = ''
        for k in k_values:
            try:
                l = li.index(str(k))
                first_index = li[l]
                li[l] = 'X'
                break
            except:
                pass

        for k in k_values:
            try:
                l = li.index(str(k))
                second_index = li[l]
                li[l] = 'X'
                break
            except:
                pass

        total += int(first_index)*10 + int(second_index)

    print(f"Svar: {total}")