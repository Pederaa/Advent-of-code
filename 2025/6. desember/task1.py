with open("2025\\6. desember\\input.txt") as file:
    conntents = file.readlines()
print(f"len: {len(conntents)}")

for i in range(len(conntents)):
    conntents[i] = conntents[i].split()

total_value = 0
for col in range(len(conntents[0])):

    temp = 0
    if conntents[-1][col] == "+":
        for i in range(len(conntents)-1):
            print(conntents[i][col], end="")
            print(" + ", end="")
            temp += int(conntents[i][col])

    elif conntents[-1][col] == "*":
        temp = 1
        for i in range(len(conntents)-1):
            print(conntents[i][col], end="")
            print(" * ", end="")
            temp *= int(conntents[i][col])
    
    else:
        raise ValueError(f"Operand not recognised:  {conntents[-1][col]}")
    
    print(f" = {temp}")
    print()
    print()
    total_value += temp

print(f"Svar: {total_value}")