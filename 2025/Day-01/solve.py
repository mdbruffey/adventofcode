import time

val = {
    "L": -1,
    "R": 1,
}

def part1(data):
    pos = 50
    count = 0
    for line in data:
        dir = line[0]
        dist = int(line[1:])
        pos = (pos + dist*val[dir]) % 100
        if pos == 0:
            count += 1
    return count

def part2(data):
    pos = 50
    count = 0
    for line in data:
        start = pos
        dir = line[0]
        dist = int(line[1:])
        count += dist // 100 #Add number of complete turns
        pos += (dist % 100)*val[dir]
        #The second part of this comparison avoids extra counting when you start at zero
        if pos >= 100 or (pos <= 0 and start != 0):
            count += 1
        pos = pos % 100
    return count


with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")