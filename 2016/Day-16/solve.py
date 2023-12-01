import time
import numpy as np

def part1(data):
    fill = "0"*(32-len(data))
    print(fill+data)
    b = bin(~np.uint32(int(data, 2)))[2:]
    print(b)
    


def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")