def generate_sequence(start):
    i = 0
    sequence = ""
    while i < len(start):
        count = 1
        while i < len(start)-1 and start[i] == start[i+1]:
            count += 1
            i += 1
        sequence += str(count) + start[i]
        i += 1
    return sequence


def part1(sequence):
    for i in range(40):
        sequence = generate_sequence(sequence)

    return len(sequence)

def part2(sequence):
    for i in range(50):
        sequence = generate_sequence(sequence)

    return len(sequence)

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")