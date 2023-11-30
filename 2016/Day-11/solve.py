import time
import random

def reset(data):
    floors = {}
    for key, value in data.items():
        new = []
        for item in value:
            new.append(item)
        floors[key] = new
    return floors

def is_fried(chip, floor, elevator, floors):
    flavor = chip.split("-")[0]
    for item in floors[floor] + elevator:
        if flavor in item and item != chip:
            return False
    for item in floors[floor] + elevator:
        if "g" in item:
            return True
    return False

def do_random_action(elevator, floor, floors):
    for i in range(len(elevator)):
        if random.randint(0,1):
            floors[floor].append(elevator.pop(random.choice(range(len(elevator)))))
    for i in range(2-len(elevator)):
        if random.randint(0,1):
            if len(floors[floor]):
                elevator.append(floors[floor].pop(random.choice(range(len(floors[floor])))))
    if not len(elevator):
        elevator.append(floors[floor].pop(random.choice(range(len(floors[floor])))))
    new_floor = random.choice([x+1 for x in range(4) if x+1 != floor])
    for i in range(floor, new_floor, int((new_floor-floor)/abs(new_floor-floor))):
        for item in floors[i] + elevator:
            if "-m" in item:
                if is_fried(item, i, elevator, floors):
                    print(f"Something fried...")
                    return -1
    return new_floor

def part1(data):
    total_items = sum([len(x) for x in data.values()])
    print(total_items)
    min_steps = 10000
    for i in range(1):
        floors = reset(data)
        print(f"Attempt {i}: ",end="")
        steps = 0
        elevator = []
        curr_floor = 1
        while True:
            if steps > min_steps:
                break
            if len(floors[4]) == total_items:
                break
            curr_floor = do_random_action(elevator, curr_floor, floors)
            if curr_floor < 1:
                steps = 1000000
            steps += 1
        if steps < min_steps:
            min_steps = steps
        
    return min_steps

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

num_convert = {"first": 1,
               "second": 2,
               "third": 3,
               "fourth": 4}

floors = {}
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
                stuff[i] = thing.split("-")[-2].split()[-1] + "-m"
            if "generator" in thing:
                stuff[i] = thing.split()[-2] + "-g"
        floors[floor] = stuff
    else:
        floors[floor] = []


start = time.perf_counter()
res1 = part1(floors)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")