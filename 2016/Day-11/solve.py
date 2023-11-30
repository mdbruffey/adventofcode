import time
import itertools

def distance_from_target(state, target):
    count = 0
    for i in range(1,len(state[1:-1])):
        count += target[i]-state[i]
    return count

def is_fried(chip, items):
    flavor = chip.split("-")[0]
    for item in items:
        if flavor in item and item != chip:
            return False
    for item in items:
        if "-g" in item:
            return True
    return False

def make_move(move, state, rtgs):
    #print(f"Making move {move} from {state}")
    shift = move[0]
    direction = int(shift/abs(shift))
    floor = state[0]
    target_floor = floor + shift
    steps = state[-1]

    for i in range(floor+direction, target_floor + direction, direction):
        steps += 1
        items = [key for key in rtgs if state[rtgs[key]]==i or rtgs[key] in move[1:]]
        #print(f"{items} on floor {i}")
        for item in items:
            if "-m" in item:
                if is_fried(item, items):
                    #print(f"Something fried...")
                    return None
                
    new = [target_floor]            
    for i in range(1,len(rtgs)+1):
        if i in move[1:]:
            new.append(state[i] + shift)
        else:
            new.append(state[i])
    new.append(steps)
    return tuple(new)

def find_moves(state):
    moves = []
    floor = state[0]
    items = [i for i in range(1,len(rtgs)+1) if state[i] == floor]
    for i in range(1,5):
        if i == floor:
            continue
        for index in items:
            moves.append((i-floor, index))
        for index in itertools.combinations(items,2):
            moves.append((i-floor,index[0],index[1]))
    return moves

def part1(initial_state, target, rtgs):
    queue = [initial_state]
    visited = set()
    min_distance = 1000
    criteria = distance_from_target(initial_state, target) // 10
    print(criteria)
    while queue:
        state = queue.pop(0)
        if state[:-1] == target:
            return state[-1]
        
        for move in find_moves(state):
            next = make_move(move, state, rtgs)
            if next and next not in visited:
                distance = distance_from_target(next, target)
                if distance < min_distance:
                    min_distance = distance
                if distance - min_distance > criteria:
                    continue
                queue.append(next)
                visited.add(next)

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

num_convert = {"first": 1,
               "second": 2,
               "third": 3,
               "fourth": 4}
index = iter(range(100))
rtgs = {}
for line in data:
    floor, stuff = line.split(" floor contains ")
    floor = num_convert[floor.split()[-1]]
    if floor != 4:
        if "," in stuff:
            stuff = stuff.split(", ")
        else:
            stuff = stuff.split(" and ")
        for i, thing in enumerate(stuff):
            if "microchip" in thing:
                thing = thing.split("-")[-2].split()[-1] + "-m"
            if "generator" in thing:
                thing = thing.split()[-2] + "-g"
            rtgs[thing] = floor

initial_state = [1]
next(index)
for item, floor in rtgs.items():
    initial_state.append(floor)
    rtgs[item] = next(index)
initial_state.append(0)

#state tuple lists the floors of each item and ends with the number of steps taken
#(elevator, item 1, item 2, ..., item n, steps)
initial_state = tuple(initial_state)
target_state = []
for i in range(len(rtgs)+1):
    target_state.append(4)
target_state = tuple(target_state)
print(rtgs)

start = time.perf_counter()
res1 = part1(initial_state, target_state, rtgs)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")