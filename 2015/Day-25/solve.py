import time

def iterate(code):
    return (code*252533) % 33554393

#This is an implementation of the Right-to-left binary method
#for modular exponentiation
def fast_iterate(c, e):
    base = 252533
    mod = 33554393
    while e > 0:
        if e % 2 == 1:
            c = (c*base) % mod
        e = e >> 1
        base = (base*base) % mod
    return c

def find_sequence_position(coords):
    row, col = coords
    n = int(row*(row-1)/2) + 1
    for j in range(row+1, row+col):
        n+= j
    return n

def part1(coords):
    n = find_sequence_position(coords)
    code = 20151125
    for i in range(n-1):
        code = iterate(code)
    return code

def part2(coords):
    row, col = coords
    n = int((row + col -2)*(row+col-1)/2 + col - 1)
    code = 20151125
    return fast_iterate(code, n)

with open("input.txt") as file:
    data = file.read()

coords = list(map(int,data.strip("\n").split(" row ")[1].replace(" column ", "").strip(".").split(",")))

start = time.perf_counter()
res1 = part1(coords)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(coords)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")