import time

def rotate(l, steps):
    return chr((ord(l)-97 + steps)%26 + 97) 

def part1(data):
    count = 0
    for line in data:
        counts = {}
        for char in line[0][:-3]:
            if char == "-":
                continue
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        items = sorted(counts.items(), key = lambda x: (-x[1],x[0]))
        if "".join([items[i][0] for i in range(5)]) == line[1]:
            count += int(line[0][-3:])
        
    return count


def part2(data):
    for line in data:
        name = line[0][:-3]
        id = int(line[0][-3:])
        decrypt = ""
        for char in name:
            if char == "-":
                decrypt += " "
            else:
                decrypt += rotate(char, id)
        if "north" in decrypt:
            return id


with open("input.txt") as file:
    raw = file.readlines()

data = []
for line in raw:
    line = line.split("[")
    line[1] = line[1].strip("]\n")
    data.append(line)


start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")