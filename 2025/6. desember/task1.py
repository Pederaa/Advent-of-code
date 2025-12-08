with open("2025\\6. desember\\input.txt") as file:
    conntents = file.readlines()

for i in range(len(conntents)):
    conntents[i] = conntents[i].split(" ")

print(conntents[1])

total_value = 0
for col in range(len(conntents[0])-1):

    temp = 0
    if conntents[-1][col] == "+":
        for i in range(len(conntents)-1):
            temp += int(conntents[i][col])

    elif conntents[-1][col] == "-":
        for i in range(len(conntents)-1):
            temp -= int(conntents[i][col])

    elif conntents[-1][col] == "*":
        for i in range(len(conntents)-1):
            temp *= int(conntents[i][col])
    
    else:
        raise ValueError(f"Operand not recognised:  {conntents[-1][col]}")
    
    total_value += temp

print(f"Svar: {total_value}")