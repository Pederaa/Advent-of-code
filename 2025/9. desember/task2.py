def isInBox(c1, c2, P):
    if (int(P[0]) - int(c1[0]))*(int(P[0])-int(c2[0])) < 0:
        return False
    
    if (int(P[1]) - int(c1[1]))*(int(P[1]) - int(c2[1])) < 0:
        return False

    return True


if __name__ == "__main__":
    with open("..\\Advent of code inputs\\2025\\9.txt") as file:
        contents = file.readlines()

    max_area = 0
    for i in range(len(contents)-1):
        print(f"i: {i}")
        for j in range(i, len(contents)):
            c1 = contents[i].split(",")
            c2 = contents[j].split(",")
            for k in range(1, len(contents)):
                P = contents[k-1].split(",")
                Q = contents[k].split(",")

                p = isInBox(c1, c2, P)
                q = isInBox(c1, c2, Q)

                if p and not q:
                    break
                elif not p and q:
                    break

                max_area = max(max_area, abs(int(c1[0]) - int(c2[0]) + 1))*(abs(int(c1[1]) - int(c2[1]) + 1))

    print(f"Svar: {max_area}")