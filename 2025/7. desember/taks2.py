with open("2025\\7. desember\\input.txt") as file:
    env = file.readlines()

for i in range(len(env)):
    g = list(env[i])
    env[i] = g

beamPos = []
first = env[0].index('S')

beamPos.append([1, first])
env[1][first] = 1

c = 0
total = 0
beamSedstroyedPos = []
while len(beamPos) > 0 and c < 1000000:
    c += 1

    y, x = beamPos[0]
    
    try:
        num = int(env[y][x])
    except:
        raise ValueError(f"{env[y][x]} is not intable")

    if y+1 >= len(env):
        if x not in beamSedstroyedPos:
            total += num
            beamSedstroyedPos.append(x)
            env[y][x] = num
        
        del beamPos[0]

    elif env[y+1][x] == "^":
        
        yl, xl = (y+1, x-1)
        if [yl, xl] not in beamPos and xl >= 0:
            g = env[yl][xl]

            if type(g) == type(int()):
                env[yl][xl] = num + g
            else:
                env[yl][xl] = num
            
            beamPos.append([yl, xl])

        yr, xr = (y+1, x+1)
        if [yr, xr] not in beamPos and xr >= 0:
            g = env[yr][xr]
            if type(g) == type(int()):
                env[yr][xr] = num + g
            else:
                env[yr][xr] = num

            beamPos.append([yr, xr])

        del beamPos[0]
    

    elif env[y+1][x] == ".":
        env[y+1][x] = num

        beamPos[0] = [y+1, x]
    
    elif type(env[y+1][x]) == type(int()):
        env[y+1][x] = env[y+1][x]
    
    else:
        continue
        raise ValueError(f"Symbol not recognised: {env[y+1][x]}")


print(beamPos)
print(f"count: {c}")
print(f"Svar: {total}")


print(env)