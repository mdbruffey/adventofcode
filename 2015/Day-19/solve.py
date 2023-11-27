import time

def devolve(molecule, pairs):
    for replace, target in pairs:
        if replace in molecule:
            idx = molecule.find(replace)
            return molecule[:idx] + target + molecule[idx+len(replace):]
    return molecule

def part1(molecules, options):
    molecules = set()
    for i, char in enumerate(molecule):
        if char.islower():
            continue
        if i < len(molecule)-1 and molecule[i+1].islower():
            char = char + molecule[i+1]
        if char in options:
            for option in options[char]:
                molecules.add(molecule[:i] + option + molecule[i+len(char):])

    return len(molecules)

def part2(molecule, options):
    count = 0
    inverse = {}
    for key, value in options.items():
        for replace in value:
            inverse[replace] = key
    pairs = list(inverse.items())
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    while molecule != "e":
        molecule = devolve(molecule, pairs)
        count += 1
    return count

with open("input.txt") as file:
    data = file.read()

replacements, molecule = data.split("\n\n")
replacements = replacements.split("\n")
options = {}
for replacement in replacements:
    target, replace = replacement.split(" => ")
    if target not in options:
        options[target] = [replace]
    else:
        options[target].append(replace)
starta = time.perf_counter()
res1 = part1(molecule, options)
enda = time.perf_counter()
startb = time.perf_counter()
print(f"Part 1: {res1} -- {(enda-starta):.4f} s")
res2 = part2(molecule, options)
print(f"Part 2: {res2} -- {(time.perf_counter()-startb):.4f} s")