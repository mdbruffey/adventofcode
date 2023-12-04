import time
import numpy as np
import collections

def part1(num_elves):
    string = bin(np.uint64(num_elves))[2:]
    l = num_elves - 2**(len(string)-1)
    return 2*l + 1

def part2(num_elves):
    left = collections.deque()
    right = collections.deque()
    for i in range(1, num_elves+1):
        if i < (num_elves//2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()
        right.appendleft(left.popleft())
        left.append(right.pop())

    return left[0]

with open("input.txt") as file:
    data = int(file.read())

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")