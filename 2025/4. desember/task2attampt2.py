def count_surrounding_bales(state, y, x):
    bales_num = 0
    surrounding = [state[i][max(0, x-1):min(len(state[0]), x+2)] 
                   for i in range(max(0, y-1), min(y+2, len(state)))]
    bales_num = "".join(surrounding).count("@")
    return bales_num

def remove_bales(state):
    to_remove = []

    for y in range(len(state)):
        for x in range(len(state[0])-1):
            if state[y][x] == '.':
                continue
            
            count = count_surrounding_bales(state, y, x)
            if count < 4+1:
                to_remove.append((y, x))
    
    balesToRemoveCount = 0
    for y, x in to_remove:
        state[y] = state[y][:x] + '.' + state[y][x+1:]
        balesToRemoveCount += 1

    return state, balesToRemoveCount

if __name__ == "__main__":
    with open("..\\Advent of code inputs\\2025\\4.txt") as file:
        state = file.readlines()

    c = 0
    prev_state = state
    total_removals = 0
    while state == prev_state and c < 100:
        prev_state = state
        c += 1

        state, num = remove_bales(state)
        total_removals += num

        print(f"c: {c}")
    
    print(f"Total removals: {total_removals}")
