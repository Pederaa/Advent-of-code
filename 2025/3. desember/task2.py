
def counting_sort(list): # TODO: Implement counting sort
    pass

with open("2025\\3. desember\\input.txt") as file:
    total = 0

    for line in file:
        if line[-1] == '\n':
            line = line[:-1]

        new_line = counting_sort(line)
        total += int("".join(new_line[0:12]))

    print(f"Svar: {total}")