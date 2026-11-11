import time

def part1(step):
    buffer = [0]
    pos = 0
    for i in range(1,2018):
        pos += step
        pos = (pos)%len(buffer)
        buffer = buffer[:pos+1] + [i] + buffer[pos+1:]
        pos += 1
    return buffer[pos+1]


def part2(step):
    value = None
    pos = 0
    for i in range(1,50000000):
        pos += step
        pos = pos % i
        if pos == 0:
            value = i
        pos += 1
    return value

with open("input.txt") as file:
    data = int(file.read())

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")