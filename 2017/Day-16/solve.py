import time

def part1(instructions):
    programs = [l for l in "abcdefghijklmnop"]
    for instruction in instructions:
        if instruction[0] == "s":
            length = int(instruction[1:])
            programs = programs[-length:] + programs[0:-length]
        elif instruction[0] == "x":
            idxa, idxb = list(map(int, instruction[1:].split("/")))
            programs[idxa], programs[idxb] = programs[idxb], programs[idxa]
        elif instruction[0] == "p":
            proga, progb = instruction[1:].split("/")
            idxa = programs.index(proga)
            idxb = programs.index(progb)
            programs[idxa], programs[idxb] = programs[idxb], programs[idxa]
    return "".join(programs)

def part2(instructions):
    programs = [l for l in "abcdefghijklmnop"]
    seen = []
    seen.append("".join(programs))
    for i in range(100000):
        for instruction in instructions:
            if instruction[0] == "s":
                length = int(instruction[1:])
                programs = programs[-length:] + programs[0:-length]
            elif instruction[0] == "x":
                idxa, idxb = list(map(int, instruction[1:].split("/")))
                programs[idxa], programs[idxb] = programs[idxb], programs[idxa]
            elif instruction[0] == "p":
                proga, progb = instruction[1:].split("/")
                idxa = programs.index(proga)
                idxb = programs.index(progb)
                programs[idxa], programs[idxb] = programs[idxb], programs[idxa]
        progstring = "".join(programs)
        if progstring not in seen:
            seen.append(progstring)
        else:
            break
    return seen[1000000000 % (i+1)]

with open("input.txt") as file:
    data = file.read().split(",")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")