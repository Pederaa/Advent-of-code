with open("C:\\Users\\Peder\\OneDrive - NTNU\\Dokumenter\\GitHub\\Advent of code inputs\\2025\\8.txt") as file:
    lines = file.readlines()

D = []
for i in range(len(lines)):
    x1,y1,z1 = lines[i].split(",")

    for j in range(i+1, len(lines)):
        x2,y2,z2 = lines[j].split(",")

        D.append(((i, j), (int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + ((int(z1)-int(z2))**2)))

import operator
D = sorted(D, key=operator.itemgetter(1))

def shouldMakeNewCircuit(i, j, C):
    i_t, j_t = (-1, -1)
    for k in range(len(C)):
        if i in C[k]:
            i_t = k
        elif j in C[k]:
            j_t = k
    
    return i_t, j_t

def joinListsWithSimilarItem(L, R):
    S = R
    for item in L:
        if not item in R:
            S.append(item)
    
    return S

C = []
for i in range(1000):
    i,j = D[i][0]

    i_t, j_t = shouldMakeNewCircuit(i, j, C)

    if i_t != -1 and j_t != -1:
        if i_t == j_t:
            continue
        
        C[i_t] = joinListsWithSimilarItem(C[i_t], C[j_t])
        del C[j_t] 

    elif i_t != -1 and j_t == -1:
        C[i_t].append(j)

    elif i_t == -1 and j_t != -1:
        C[j_t].append(i)

    elif i_t == -1 and j_t == -1:
        C.append([i, j])


C.sort(key=len)

res = 1
for i in range(40):
    res *= len(C[i])

print(f"Svar: {res}")