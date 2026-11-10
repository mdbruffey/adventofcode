import time

def part1(sequence):
    ring_length = 256
    ring = tuple(range(ring_length))
    i = 0
    step = 0
    for length in sequence:
        start = i % ring_length
        end = (start + length) % ring_length
        if length == 0 or length == 1:
            pass
        elif start < end:
            ring = ring[:start] + ring[start:end][::-1] + ring[end:]
        elif end == 0:
            ring = ring[:start] + ring[start:][::-1]
        else:
            section = ring[start:] + ring[:end]
            section = section[::-1]
            ring = section[-end:] + ring[end:start] + section[:-end]
        i += length + step
        step += 1
    return ring[0]*ring[1]

def part2(sequence):
    ring_length = 256
    ring = tuple(range(ring_length))
    pos = 0
    step = 0
    for _ in range(64):
        for length in sequence:
            start = pos % ring_length
            pos = start
            end = (start + length) % ring_length
            if length == 0 or length == 1:
                pass
            elif start < end:
                ring = ring[:start] + ring[start:end][::-1] + ring[end:]
            elif end == 0:
                ring = ring[:start] + ring[start:][::-1]
            else:
                section = ring[start:] + ring[:end]
                section = section[::-1]
                ring = section[-end:] + ring[end:start] + section[:-end]
            pos += length + step
            step += 1
    dense = []
    for j in range(16):
        val = ring[16*j]
        for i in range(1,16):
            val = val ^ ring[16*j + i]
        dense.append(val)
    
    form = lambda x: f"{x:02x}"
    hash = "".join(map(form,dense))
    return hash


with open("input.txt") as file:
    data = file.read().strip()
    p1 = list(map(int, data.strip().split(",")))
    p2 = list(map(ord, data)) + [17, 31, 73, 47, 23]

start = time.perf_counter()
res1 = part1(p1)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(p2)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")