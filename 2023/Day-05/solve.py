import time

def map_value(val, mapping):
    for key in mapping:
        a,b = key
        if val in range(a,b):
            dif = val-a
            return mapping[key][0] + dif
    return val

def part1(seeds, maps):
    locations = []
    for seed in seeds:
        for mapping in maps.values():
            seed = map_value(seed, mapping)
        locations.append(seed)
    return min(locations)

def part2(seeds, maps):
    lowest = 100000000000000
    
    for i in range(0,len(seeds),2):
        a = seeds[i]
        b = a + seeds[i+1]
        for seed in range(a,b):
            for mapping in maps.values():
                seed = map_value(seed, mapping)
            if seed < lowest:
                lowest = seed
                print(lowest)
    return seed

with open("input.txt") as file:
    data = file.read()

data = data.split("\n\n")
seeds = list(map(int,data[0].split(": ")[1].split()))
maps = {}
for item in data[1:]:
    mapping = {}
    title = item.split("\n")[0].split()[0]
    for line in item.split("\n")[1:]:
        nums = list(map(int, line.split()))
        a2 = nums[0]
        b2 = a2 + nums[2]
        a1 = nums[1]
        b1 = a1 + nums[2]
        mapping[(a1,b1)] = (a2, b2)
    maps[title] = mapping

start = time.perf_counter()
res1 = part1(seeds, maps)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(seeds, maps)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")