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
        
        if g == "@":
            return 1
        
        elif g == ".":
            return 0
        else:
            raise ValueError(f"Not recognised symbol: {g}")
    
    except:
        pass

    return 0


with open("..\\Advent of code inputs\\2025\\4.txt") as file:
    currentline = file.readline()
    prevline = ["." for _ in range(len(currentline))]
    nextline = file.readline()

    count = 0
    bales_that_can_be_reached = 0
    lastline = False
    while not lastline and count < 10000:
        count += 1

        if currentline[-1] == "\n":
            currentline = currentline[:-1]

        if nextline == "":
            nextline = ["." for _ in range(len(currentline)+2)]
            lastline = True

        for i in range(len(currentline)):
            if currentline[i] == ".":
                continue

            bales_num = 0
            for h in range(-1, 2):
                for j in range(-1, 2):
                    bales_num += is_bale(prevline, currentline, nextline, i, j, h)

            if bales_num < 4:
                bales_that_can_be_reached += 1

                indicies = [k for k in range(max(0, i-1), min(len(currentline), i+2))]
                
                print(f"indecies: {indicies}\t i: {i}")
                for i in indicies:
                    print(prevline[i], end="")
                print()
                for i in indicies:
                    print(currentline[i], end="")
                print()
                for i in indicies:
                    print(nextline[i], end="")

                print()
                print(f"bales_num: {bales_num}")
                print()
                print()
                print()


        prevline = currentline
        currentline = nextline
        nextline = file.readline()

    print(f"Svar: {bales_that_can_be_reached}")
