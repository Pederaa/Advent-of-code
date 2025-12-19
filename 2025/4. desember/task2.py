def is_bale(prevline, currentline, nextline, i , j, h):
    if (j == h) and j == 0:
        return 0
    elif i+h < 0:
        return 0

    try:
        if j == -1:
            g = prevline[i+h]

        elif j == 0:
            g = currentline[i+h]
        
        elif j == 1:
            g = nextline[i+h]
        else:
            raise ValueError(f"Not recognised value for j: {j}")
        
        if g == ".":
            return 0
        
        else:
            return 1
    
    except:
        pass

    return 0

def count_surrounding_bales(prevline, currentline, nextline, i):
    bales_num = 0
    for h in range(-1, 2):
        for j in range(-1, 2):
            bales_num += is_bale(prevline, currentline, nextline, i, j, h)
    
    if i == len(currentline)-1:
        bales_num -= 1

    return bales_num

def apply_func_ontable(func, contents):
    currentline = contents[0]
    prevline = ["." for _ in range(len(currentline))]
    nextline = contents[1]
    num = 0

    for k in range(len(contents)):
        if currentline[-1] == "\n":
            currentline = currentline[:-1]

        try:
            nextline = contents[k+1]
        except:
            nextline = ["." for _ in range(len(currentline))]

        for i in range(len(currentline)):
            if currentline[i] == ".":
                continue
            
            try:
                to_instert, num = func(prevline, currentline, nextline, i)
            except ValueError:
                to_instert = func(prevline, currentline, nextline, i)

            left = currentline[:i]
            right = currentline[i+1:]
            currentline = left + str(to_instert) + right

            contents[k] = currentline

        prevline = currentline
        currentline = nextline
    
    return contents, num


def translate_to_numbers(contents):
    pass

def remove_bale(prevline, currentline, nextline, i):
    pass

def is_going_to_remove(prevline, currentline, nextline, i):
    try: 
        if int(currentline[i]) < 4:
            remove_bale(prevline, currentline, nextline, i)
    
    except ValueError:
        pass
    return currentline[i]

if __name__ == "__main__":
    with open("..\\Advent of code inputs\\2025\\4.txt") as file:
        contents = file.readlines()

    contents, num = apply_func_ontable(count_surrounding_bales, contents)
    print(contents)

    c = 0
    prev = 0
    total_removals = 0
    while contents != prev and c < 10000:
        prev = contents
        c += 1

        contents, num = apply_func_ontable(is_going_to_remove, contents)
        total_removals += num
    
    print(f"Total removals: {total_removals}")
