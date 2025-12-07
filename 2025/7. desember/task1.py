
with open("2025\\7. desember\\input.txt") as file:
    env = file.readlines()

beamPos = []
first = env[0].find("S")

beamPos.append([1, first])

c = 0
totalBeams = 0
beamSedstroyedPos = []
while len(beamPos) > 0 and c < 1000000:
    c += 1
    #print(f"list: {beamPos}")

    y, x = beamPos[0]
    if y+1 >= len(env):
        if x not in beamSedstroyedPos:
            print(f"Beam destroyed at {x}")
            totalBeams += 1
            beamSedstroyedPos.append(x)
        
        del beamPos[0]
        continue

    # print(f"y:{y} x:{x} under: {env[y+1][x]}", end="")

    # print(env[y])
    if env[y+1][x] == "^":
        if [y+1, x+1] not in beamPos and x+1 <= len(env[0]):
            beamPos.append([y+1, x+1])
        if [y+1, x-1] not in beamPos and x-1 >= 0:
            beamPos.append([y+1, x-1])

        del beamPos[0]
    
    elif env[y+1][x] == ".":
        y = y+1
        beamPos[0] = [y, x]

beamSedstroyedPos.sort()
print(beamSedstroyedPos)
print(f"{len(env)}, {len(env[0])}")
print(f"Svar: {totalBeams}")