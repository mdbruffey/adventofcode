import time

def part1(data):
    blocks = data[::2]
    space = data[1::2]
    i = 0
    disk = []
    while i < len(blocks) and i < len(space):
        disk.extend([i]*int(blocks[i]))
        disk.extend(["."]*int(space[i]))
        i += 1
    if i < len(blocks):
        disk.extend([i]*int(blocks[i]))
    j = len(disk)-1
    count = 0
    for i in range(len(disk)-disk.count(".")):
        if disk[i] == ".":
            while disk[j] == ".":
                j -= 1
            disk[i], disk[j] = disk[j], disk[i]
        count += i*disk[i]
    return count

def part2(data):
    blocks = data[::2]
    space = data[1::2]
    i = 0
    disk = []
    sizes = {}
    while i < len(blocks) and i < len(space):
        disk.extend([i]*int(blocks[i]))
        sizes[i] = int(blocks[i])
        disk.extend(["."]*int(space[i]))
        i += 1
    if i < len(blocks):
        disk.extend([i]*int(blocks[i]))
        sizes[i] = int(blocks[i])
    
    for id in sorted(sizes,reverse=True):
        index = disk.index(id)
        size = sizes[id]
        i = disk.index(".") #starting at the first index with space saves 5 seconds
        while i < index:
            if disk[i] == ".":
                space = 1
                while disk[i+space] == ".":
                    space += 1
                if space >= size:
                    for j in range(size):
                        disk[i+j], disk[index+j] = disk[index+j], disk[i+j]
                    break
                else:
                    i += space
            else:
                i += 1
    count = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            count += i*disk[i]
    return count
            

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")