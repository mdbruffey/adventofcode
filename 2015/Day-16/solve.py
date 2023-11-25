mfcsam = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

def check_sue(sue):
    for req in sue:
        req, num = req.split(": ")
        num = int(num)
        if mfcsam[req] != num:
            return False
    return True

def improved_check_sue(sue):
    for req in sue:
        req, num = req.split(": ")
        num = int(num)
        if req in ["cats","trees"]:
            if mfcsam[req] >= num:
                return False
        elif req in ["pomeranians","goldfish"]:
            if mfcsam[req] <= num:
                return False
        else:
            if mfcsam[req] != num:
                return False
    return True

def part1(sues):
    for sue in sues:
        if check_sue(sues[sue]):
            return sue

def part2(data):
    for sue in sues:
        if improved_check_sue(sues[sue]):
            return sue

with open("input.txt") as file:
    data = file.readlines()

sues = {}
for line in data:
    line = line.strip("\n")
    sue = line[4:line.find(":")]
    results = line[line.find(":")+2:].split(", ")
    sues[sue] = results

res1 = part1(sues)
res2 = part2(sues)
print(f"Part 1: {res1}\nPart 2: {res2}")