def calculate_wrapping(box):
    return 2*(box[0]*box[1] + box[0]*box[2] + box[1]*box[2]) + box[0]*box[1]

def measure_ribbon_length(box):
    return 2*(box[0] + box[1]) + box[0]*box[1]*box[2]

def part1(data):
    boxes = []
    for line in data:
        box = line.split("x")
        box = list(map(int, box))
        box.sort()
        boxes.append(box)
    
    area = 0
    for box in boxes:
        area += calculate_wrapping(box)

    return area

def part2(data):
    boxes = []
    for line in data:
        box = line.split("x")
        box = list(map(int, box))
        box.sort()
        boxes.append(box)
    
    length = 0
    for box in boxes:
        length += measure_ribbon_length(box)

    return length

with open("input.txt") as file:
    lines = file.readlines()

res1 = part1(lines)
res2 = part2(lines)
print(f"Part 1: {res1}\nPart 2: {res2}")