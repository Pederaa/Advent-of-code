with open("C:\\Users\\Peder\\OneDrive - NTNU\\Dokumenter\\GitHub\\Advent of code inputs\\2025\\8.txt") as file:
    points = file.readlines()

D = []
for i in range(len(points)):
    x1,y1,z1 = points[i].split(",")

    for j in range(i+1, len(points)):
        x2,y2,z2 = points[j].split(",")

        D.append(((i, j), (int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + ((int(z1)-int(z2))**2)))

import operator
D = sorted(D, key=operator.itemgetter(1))


def findParent(i, P):
    if P[i] == i:
        return i
    
    return findParent(P[i], P)


P = [i for i in range(len(points))]

for d in range(1000):
    i, j = D[d][0]

    i_rep = findParent(i, P)
    j_rep = findParent(j, P)
    if i_rep != j_rep:
        P[i_rep] = j_rep

E = [0 for _ in range(len(points))]

for p in range(len(P)):
    E[findParent(p, P)] += 1

E = sorted(E)

summ = 1*E[-1]*E[-2]*E[-3]
print(f"Svar: {summ}")