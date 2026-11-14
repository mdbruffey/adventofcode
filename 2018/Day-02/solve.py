import time

def part1(data):
    two = 0
    three = 0
    for line in data:
        letters = set(line)
        has2 = False
        has3 = False
        for letter in letters:
            if line.count(letter) == 2:
                has2 = True
            elif line.count(letter) == 3:
                has3 = True
        two += has2
        three += has3
    return two*three

def part2(data):
    for i in range(len(data[0])):
        seen = set()
        for id in data:
            id = id[:i] + id[i+1:]
            if id not in seen:
                seen.add(id)
            else:
                return id


with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")