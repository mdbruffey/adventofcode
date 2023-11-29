import time

def part1(data):
    result = ""
    for i in range(len(data[0])):
        counts = {}
        for char in [row[i] for row in data]:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        result += list(filter(lambda x: x[1] == max(counts.values()), list(counts.items())))[0][0]
    return result

def part2(data):
    result = ""
    for i in range(len(data[0])):
        counts = {}
        for char in [row[i] for row in data]:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        result += list(filter(lambda x: x[1] == min(counts.values()), list(counts.items())))[0][0]
    return result

with open("input.txt") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] =  data[i].strip("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")