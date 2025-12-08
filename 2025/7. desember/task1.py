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
            env[y] = env[y][:x] + "|" + env[y][x+1:]
        
        del beamPos[0]
        continue

    if env[y][x] == "^":
        split += 1
        #env[y] = env[y][:x] + "|" + env[y][x+1:]
        if [y, x+1] not in beamPos and x+1 <= len(env[0]):
            beamPos.append([y, x+1])

        if [y, x-1] not in beamPos and x-1 >= 0:
            beamPos.append([y, x-1])

        del beamPos[0]
    
    elif env[y][x] == ".":
        env[y] = env[y][:x] + "|" + env[y][x+1:]
    
        y = y+1
        beamPos[0] = [y, x]
    
    elif env[y][x] == "|":
        del beamPos[0]

print(beamPos)
print(f"count: {c}")
print(f"Svar: {split}")

print(env)