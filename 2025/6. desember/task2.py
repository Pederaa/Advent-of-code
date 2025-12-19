def find_j(operations, i):
    for j in range(i+1, len(operations)):
        if operations[j] != " ":
            return j
    
    return -1

def sumthethingy(contents, i, j, operation):
    print(f"i: {i} \t j: {j}")
    partial_sum = 0
    if operation == "*":
        partial_sum = 1

    for k in range(i, j-1):
        for l in range(len(contents)-1):
            temp[l] = contents[l][k]
        
        if operation == "*":
            partial_sum *= int("".join(temp))
            print(f"{int(''.join(temp)) } * ", end="")
        elif operation == "+":
            partial_sum += int(''.join(temp))
            print(f"{int(''.join(temp))} + ", end="")

    print(f" = {partial_sum}")
    print()

    return partial_sum


with open("..\\Advent of code inputs\\2025\\6.txt") as file:
    contents = file.readlines()

operations = contents[-1]

i = 0
j = find_j(operations, i)
c = 0

total = 0

while j != -1 and c < 10000:
    c += 1
    temp = ["" for _ in range(len(contents))]

    temp2 = 0

    operation = operations[i]

    partial_sum = sumthethingy(contents, i, j, operation)

    total += partial_sum
    i = j
    j = find_j(operations, i)

operation = operations[i]
total += sumthethingy(contents, i, len(contents[0]), operation)

print(f"Svar: {total}")