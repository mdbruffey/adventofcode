import time
import itertools

def part1(num_elves):
    elves = [i+1 for i in range(num_elves)]
    dif = 0
    while len(elves) > 1:
        if dif == 1:
            dif = (dif + len(elves)%2) % 2
            elves = elves[1::2]
        else:
            dif = (dif + len(elves)%2) % 2
            elves = elves[::2]

    return elves[0]

def part2(num_elves):
    elves = [i+1 for i in range(num_elves)]
    index = len(elves)//2
    i = 0
    while len(elves) > 1:
        i += 1
        if len(elves) == 2:
            elves.pop((index+1)%len(elves))
        else:
            elves.pop(index)
        index = (i%len(elves) + len(elves)//2)%len(elves)
    return elves[0]

with open("input.txt") as file:
    data = int(file.read())

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")