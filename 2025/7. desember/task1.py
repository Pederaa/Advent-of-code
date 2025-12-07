
with open("2025\\7. desember\\input.txt") as file:
    env = file.readlines()

beamPos = []
first = env[0].find("S")

beamPos.append([1, first])

c = 0
totalBeams = 0
split = 0
beamSedstroyedPos = []
while len(beamPos) > 0 and c < 1000000:
    c += 1

    y, x = beamPos[0]
    if y+1 >= len(env):
        if x not in beamSedstroyedPos:
            totalBeams += 1
            beamSedstroyedPos.append(x)
        
        del beamPos[0]
        continue

    if env[y+1][x] == "^":
        split += 1
        if [y+1, x+1] not in beamPos and x+1 <= len(env[0]):
            beamPos.append([y+1, x+1])

        if [y+1, x-1] not in beamPos and x-1 >= 0:
            beamPos.append([y+1, x-1])

        del beamPos[0]
    
    elif env[y+1][x] == ".":
        left = env[y+1][:x]
        right = env[y+1][x+1:]
        # env[y+1] = left + "|" + right

        # print(f"Gammel: {}")
    
        y = y+1
        beamPos[0] = [y, x]

print(f"count: {c}")
print(f"Svar: {split}")