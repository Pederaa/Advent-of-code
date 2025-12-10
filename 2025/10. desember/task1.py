from functools import cache

def pressButton(indicator, button):
    button = button.strip()[1:-1]
    indicies = button.split(",")

    for ind in indicies:
        if indicator[int(ind)] == '#':
            indicator[int(ind)] = '.'
        elif indicator[int(ind)] == '.':
            indicator[int(ind)] = '#'
        else:
            raise ValueError(f"Unrecognised symbol: {indicator[int(ind)]}")
    
    return indicator

@cache
def tryPressingButton(indicator, buttons, sol):
    if indicator == sol:
        return 1
    if len(buttons) == 0:
        return 0

    temp = buttons.split(" ")
    min_switches = 200
    for button in buttons.split(" "):
        print(button)
        temp.remove(button)
        res = tryPressingButton(indicator, " ".join(temp), sol)
        
        if res != 0:
            min_switches = min(min_switches, res+1)
        
        temp = buttons.split(" ")
    
    if min_switches == 200:
        raise ValueError(f"Fant ingen løsning")

    print(min_switches)
    return min_switches


with open("2025\\10. desember\\input.txt") as file:
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
        
    temp = tryPressingButton(indicator, buttons, sol)
    total += temp
    break

print(f"svar: {total}")
