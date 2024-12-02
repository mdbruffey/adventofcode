import time

def is_safe(report):
    ascending = report[0] < report[1]
    for i in range(len(report)-1):
        if ascending and report[i] >= report[i+1]:
            return False
        elif (not ascending) and report[i] <= report[i+1]:
            return False
        elif abs(report[i]-report[i+1]) > 3:
            return False
    return True

def dampened(report):
    for i in range(len(report)):
        if is_safe(report[:i]+report[i+1:]):
            return True
    return False

def part1(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count

def part2(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count +=1
        elif dampened(report):
                count += 1
    return count

with open("input.txt") as file:
    data = file.read()
    data = data.splitlines()
    reports = [list(map(int,line.split())) for line in data]


start = time.perf_counter()
res1 = part1(reports)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.5f} s")
start = time.perf_counter()
res2 = part2(reports)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.5f} s")