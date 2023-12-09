import time

def part1(data):
    count = 0
    for i in range(len(data)):
        if data[i] == data[(i+1)%len(data)]:
            count += int(data[i])
    return count

def part2(data):
    count = 0
    for i in range(len(data)):
        if data[i] == data[(i+len(data)//2)%len(data)]:
            count += int(data[i])
    return count
    

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")