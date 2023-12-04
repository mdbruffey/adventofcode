import time

full_traps = ["^^.",
              ".^^",
              "^..",
              "..^"]

def get_next_row(row):
    new = ""
    for i in range(len(row)):
        if i-1 < 0:
            tiles = row[i:i+2]
            if tiles == "^^" or tiles == ".^":
                new += "^"
            else:
                new += "."
        elif i+1 >= len(row):
            tiles = row[i-1:]
            if tiles == "^^" or tiles == "^.":
                new += "^"
            else:
                new += "."
        else:
            tiles = row[i-1:i+2]
            if tiles in full_traps:
                new += "^"
            else:
                new += "."
    return new
        

def part1(row, num_rows):
    count = row.count(".")
    for i in range(num_rows-1):
        row = get_next_row(row)
        count += row.count(".")
    return count

def part2(row, num_rows):
    count = row.count(".")
    for i in range(num_rows-1):
        row = get_next_row(row)
        count += row.count(".")
    return count

with open("input.txt") as file:
    row = file.read()

num_rows = 40

start = time.perf_counter()
res1 = part1(row, num_rows)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(row, 400000)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")