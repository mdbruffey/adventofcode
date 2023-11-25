def part1(molecule, options):
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
    pass

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

res1 = part1(molecule, options)
res2 = part2(molecule, options)
print(f"Part 1: {res1}\nPart 2: {res2}")