import time

def part1(rectangles):
    seen = set()
    overlapped = set()
    for rectangle in rectangles:
        x, y = rectangle["coords"]
        w, h = rectangle["dims"]
        points = set([(i,j) for i in range(x,x+w) for j in range(y,y+h)])
        overlapped.update(seen & points)
        seen.update(points)
    return len(overlapped)

def overlaps(rect, rectangles):
    ax, ay = rect["coords"]
    aw, ah = rect["dims"]
    for r in rectangles:
        if r["id"] == rect["id"]:
            continue
        bx, by = r["coords"]
        bw, bh = r["dims"]
        if not (ax + aw <= bx or ay+ah <= by or bx+bw <= ax or by+bh <= ay):
            return True

def part2(rectangles):
    for rect in rectangles:
        if not overlaps(rect, rectangles):
            return rect["id"]
    return None

with open("input.txt") as file:
    data = file.read().split("\n")
rectangles = []
for line in data:
    id, line = line.split(" @ ")
    coords, dims = line.split(": ")
    coords = tuple(map(int,coords.split(",")))
    dims = tuple(map(int, dims.split("x")))
    rectangles.append({"id": id, "coords": coords, "dims": dims})

start = time.perf_counter()
res1 = part1(rectangles)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(rectangles)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")