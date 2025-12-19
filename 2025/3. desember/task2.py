def find_largest_left(id, n):
    print(f"id: {id}")
    maxid = 0
    for i in range(len(id)-n):
        if id[i] > id[maxid]:
            maxid = i
        
    if n == 0:
        return str(id[maxid])

    return str(id[maxid]) + find_largest_left(id[maxid+1:], n-1)

with open("..\\Advent of code inputs\\2025\\3.txt") as file:
    total = 0
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        
        l = int(find_largest_left(line, 12-1))
        print(f"subsum: {l}")
        total += l

    print(f"Svar: {total}")