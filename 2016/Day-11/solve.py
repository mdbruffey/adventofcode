import time

def is_fried(chip, floor, elevator, floors):
    flavor = chip.split("-")[0]
    for item in floors[floor]:
        if flavor in item:
            return False
    for item in elevator:
        if flavor in item:
            return False
    return True

def part1(floors):
    total_items = sum([len(x) for x in floors.values()])
    min_steps = 10000
    for i in range(10000):
        if len(floor["fourth"]) == total_items:
            break
        
    return min_steps

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

floors = {}
for line in data:
    floor, stuff = line.split(" floor contains ")
    floor = floor.split()[-1]
    if floor != "fourth":
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

print(floors)
        

start = time.perf_counter()
res1 = part1(floors)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")