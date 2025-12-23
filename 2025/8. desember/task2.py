def sortDistances(points):
    D = []
    
    for i in range(len(points)):
        x1,y1,z1 = points[i].split(",")

        for j in range(i+1, len(points)):
            x2,y2,z2 = points[j].split(",")

            D.append(((i, j), (x1, x2), (int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + ((int(z1)-int(z2))**2)))

    import operator
    D = sorted(D, key=operator.itemgetter(2))
    return D


def findParent(i, P):
    if P[i] == i:
        return i
    
    temp = findParent(P[i], P)
    P[i] = temp
    return temp


def areAllSameCuricuit(P):
    p_first = findParent(P[0], P)
    for p in range(len(P)):
        if findParent(p, P) != p_first:
            return False
    
    return True


def addBox(D, k, P):
    i, j = D[k][0]

    i_rep = findParent(i, P)
    j_rep = findParent(j, P)
    if i_rep != j_rep:
        P[i_rep] = j_rep

    return P


if __name__ == "__main__":
    with open("C:\\Users\\Peder\\OneDrive - NTNU\\Dokumenter\\GitHub\\Advent of code inputs\\2025\\8.txt") as file:
        points = file.readlines()
    
    D = sortDistances(points)
    P = [i for i in range(len(points))]

    k = 0
    while not areAllSameCuricuit(P) and k < 100000:
        P = addBox(D, k, P)
        k += 1
    
    x1 = int(D[k-1][1][0])
    x2 = int(D[k-1][1][1])
    prod =  x1*x2
    print(f"Svar: {prod}")
