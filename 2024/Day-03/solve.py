import time

def evaluate(op):
    op = op.strip(")(")
    try:
        l,r = map(int,op.split(","))
    except:
        print(op)
        return 0
    return l*r

def is_valid(op):
    op = op.strip(")(")
    if "," not in op:
        return False
    for char in op:
        if not char.isnumeric() and char != ",":
            return False
    return True

def part1(data):
    i = data.find("mul")
    reg = 0
    while i >= 0:
        data = data[i+3:]
        e = data.find(")")
        op = data[:e+1]
        if is_valid(op):
            reg += evaluate(op)
            data = data[e+1:]
        i = data.find("mul")
    return reg

def part2(data):
    data = data.split("don't()")
    instructions = data[0]
    for entry in data:
        i = entry.find("do()")
        if i >=0:
            entry = entry[i+4:]
            instructions += entry
    return part1(instructions)


with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")