def mapnextline(currentline, nextline):

    print(currentline)
    print(nextline)
    print()
    print()

    for i in range(len(currentline)):
        try:
            int(currentline[i])
        except:
            continue

        curr_num = currentline[i]
        next_value = nextline[i]

        if next_value == '.':
            nextline[i] = curr_num

        elif next_value == '^':
            if type(nextline[i-1]) == type(int()):
                nextline[i-1] += curr_num
            else:
                nextline[i-1] = curr_num
            
            if type(nextline[i+1]) == type(int()):
                nextline[i+1] += curr_num
            else:
                nextline[i+1] = curr_num
        
        elif type(next_value) == type(int()):
            nextline[i] += curr_num

        else:
            raise ValueError(f"Ikke gjenkjent symbol: '{next_value}'")
    
    return nextline


def initiat_env():
    with open("2025\\7. desember\\input.txt") as file:
        env = file.readlines()

    for i in range(len(env)):
        g = list(env[i])

        if g[-1] == '\n':
            g = g[:-1]

        env[i] = g


    first = env[0].index('S')
    env[1][first] = 1

    return env


if __name__ == "__main__":
    env = initiat_env()

    currentline = env[1]
    for nextline in env[2:]:
        nextline = mapnextline(currentline, nextline)
        currentline = nextline
    
    total = 0
    for i in range(len(currentline)):
        try:
            total += currentline[i]
        except:
            continue
        
    print(f"Svar: {total}")