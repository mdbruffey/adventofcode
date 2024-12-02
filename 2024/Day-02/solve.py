import time

#returns a tuple (True, True) when the report is safe
#When the report is not safe, the second entry of the tuple
#contains the starting index of the unsafe interval
def is_safe(report):
    ascending = report[0] < report[1]
    for i in range(len(report)-1):
        if ascending and report[i] >= report[i+1]:
            return False, i
        elif (not ascending) and report[i] <= report[i+1]:
            return False, i
        elif abs(report[i]-report[i+1]) > 3:
            return False, i
    return True, True


#Takes in a bad report and the starting index of the unsafe interval.
#Operates on the basis that either the start or end of the interval is the
#problem, so checks the report with those 2 removed. Also considers that
#the very first level could be faulty, which could have incorrectly indicated
#that the report was ascending or descending, so it always tries removing that
#first.
def dampened(report, idx):
    for i in [0,idx,idx+1]:
        if is_safe(report[:i]+report[i+1:])[0]:
            return True
    return False


def part1(reports):
    count = 0
    for report in reports:
        if is_safe(report)[0]:
            count += 1
    return count

def part2(reports):
    count = 0
    for report in reports:
        safe, i = is_safe(report)
        if safe:
            count +=1
        elif dampened(report, i):
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