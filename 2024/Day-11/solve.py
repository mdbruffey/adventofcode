import time

def blink(stones):
    new = {}
    for num in stones:
        length = len(str(num))
        if num == 0:
            new[1] = new.get(1,0) + stones[num]
        elif length%2 == 0:
            first = int(str(num)[:length//2])
            second = int(str(num)[length//2:])
            new[first] = new.get(first,0) + stones[num]
            new[second] = new.get(second,0) + stones[num]
        else:
            new[num*2024] = new.get(num*2024,0) + stones[num]
    return new

def fast_blink(stones, start):
    curr = start
    while True:
        num = stones[curr]["number"]
        next = stones[curr]["next"]
        length = len(str(num))
        if num == 0:
            stones[curr]["number"] = 1
        elif length%2 == 0:
            first = int(str(num)[:length//2])
            second = int(str(num)[length//2:])
            stones[curr]["number"] = first
            new_id = id()
            stones[curr]["next"] = new_id
            stones[new_id] = {"number":second,"next":next}
        else:
            stones[curr]["number"] = num*2024
        curr = next
        if not curr:
            return

def print_stones(stones, start):
    curr = start
    while True:
        print(stones[curr]["number"],end="")
        print(" ",end="")
        curr = stones[curr]["next"]
        if not curr:
            return

def part1(data):
    data = list(map(int,data.split()))
    stones = {}
    for num in data:
        stones[num] = 1
    blinks = 25
    for i in range(blinks):
        stones = blink(stones)
    
    return sum(stones.values())

def part2(data):
    data = list(map(int,data.split()))
    stones = {}
    for num in data:
        stones[num] = 1
    blinks = 75
    for i in range(blinks):
        stones = blink(stones)
    
    return sum(stones.values())

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")