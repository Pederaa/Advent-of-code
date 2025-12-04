def counting_sort(iter_list):
    count = [0]*10
    memory = [[]]*10

    for i in range(5):
        print(memory[int(iter_list[i])])
        print(int(iter_list[i]))
        print()

        count[int(iter_list[i])] += 1
        memory[int(iter_list[i])].append(i)

  
    l = 0
    k = 0
    max_batt = 12
    ku = []*len(iter_list)
    index = 9

    c = 0
    while l < max_batt and c < 10000:
        c += 1
        try:
            ku[memory[index][k]] = str(index)
            k += 1
            l += 1

        except:
            index -= 1
            k = 0
    
    return int("".join(ku))


with open("2025\\3. desember\\input.txt") as file:
    total = 0

    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        
        total += counting_sort(line)

    print(f"Svar: {total}")