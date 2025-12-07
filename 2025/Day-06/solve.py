import time

def safe_eval(string):
    for char in "._/\\\'\"()[]{}":
        if char in string:
            raise ValueError("string contains forbidden characters")
    return eval(string)

def group_numbers(ungrouped):
    groups = []
    group = []

    for number in ungrouped:
        if not number.strip():
            groups.append(group)
            group = []
        else:
            group.append(number)
    if len(group):
        groups.append(group)
    return groups

def part1(data):
    data = [line.split() for line in data]
    count = 0
    for i in range(len(data[0])):
        string = ""
        for j in range(len(data)-1):
            string += data[j][i] + data[-1][i]
        count += safe_eval(string[:-1])
    return count

def part2(data):
    operators = data[-1].split()
    transformed = ["".join([line[i] for line in data[:-1]]) for i in range(len(data[0]))]
    groups = group_numbers(transformed)
    
    count = 0
    for i, group in enumerate(groups):
        count += safe_eval(operators[i].join(group))
    return count  

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")