import time

WIDTH = 50
HEIGHT = 6

def execute(operation, old):
    new = [["." for i in range(WIDTH)] for j in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            new[i][j] = old[i][j]
    if "rect" in operation:
        width, height = list(map(int, operation.split(" ")[1].split("x")))
        for i in range(height):
            for j in range(width):
                new[i][j] = "#"
    elif "rotate row" in operation:
        row, amount = list(map(int, operation.split("=")[1].split(" by ")))
        for j in range(WIDTH):
            new[row][(j+amount)%WIDTH] = old[row][j]
    elif "rotate column" in operation:
        col, amount = list(map(int, operation.split("=")[1].split(" by ")))
        for i in range(HEIGHT):
            new[(i+amount)%HEIGHT][col] = old[i][col]
    return new

def part1(data):
    screen = [["." for i in range(WIDTH)] for j in range(HEIGHT)]
    for operation in data:
        screen = execute(operation, screen)
    count = 0
    for row in screen:
        count += row.count("#")
        print("".join(row))
    return count

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")