import time

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def turn(pos, dir, map):
    i, j = pos
    idx = directions.index(dir)
    for dir in [directions[idx -1], directions[(idx+1)%4]]:
        di, dj = dir
        if i+di >= len(map) or j+dj >= len(map[0]):
            continue
        if map[i+di][j+dj] != " ":
            return dir
    print("Uh, oh")
    print(pos, dir)

def part1(map):
    steps = 1
    seen = ""
    idx = map[0].find("|")
    pos = (0, idx)
    dir = directions[2]
    while True:
        i = pos[0] + dir[0]
        j = pos[1] + dir[1]
        next = map[i][j]
        if next != " ":
            pos = (i,j)
            steps += 1
            if next.isalpha():
                seen += next
            if next == "+":
                dir = turn(pos, dir, map)
        else:
            break
    return seen, steps
def part2(map):
    pass

with open("input.txt") as file:
    map = file.read().split("\n")

start = time.perf_counter()
res1, res2 = part1(map)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
part2(map)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")