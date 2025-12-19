from functools import cache

def pressButton(indicator, button):
    button = button.strip()[1:-1]
    indicies = button.split(",")
    print(f"indicies: {indicies} \t button: {button}")

    temp = ""
    for ind in range(len(indicies)):
        print("Hei")
        if indicator[int(ind)] == "#":
            temp = temp + "."
        elif indicator[int(ind)] == ".":
            temp = temp + "#"
        else:
            raise ValueError(f"Unrecognised symbol: {indicator[int(ind)]}")
    
    print(f"Temp: {temp}")
    return temp

def find_fewest_presses(indicator, buttons, sol):
    que = []
    buttons = buttons.split()
    for button in buttons:
        new_indicator = pressButton(indicator, button)
        que.append((new_indicator, 1))

    c = 0
    while len(que) != 0 and c < 2:
        c += 1
        indicator, presses = que[0]

        print(f"que: {que}")

        for button in buttons:
            new_indicator = pressButton(indicator, button)

            if new_indicator == sol:
                return presses
            
            que.append((new_indicator,  presses+1))
        
        del que[0]

if __name__ == "__main__":
    with open("..\\Advent of code inputs\\2025\\10.txt") as file:
        contents = file.readlines()

    total = 0
    for line in contents:
        i1, i2 = line.find("["), line.find("]")
        c1, c2 = line.find("("), line.find("{")

        indicator = line[i1+1:i2]
        buttons = line[c1:c2-1]

        sol = ""
        for _ in range(len(indicator)):
            sol += "."
            
        temp = find_fewest_presses(indicator, buttons, sol)
        total += temp
        break

    print(f"svar: {total}")
