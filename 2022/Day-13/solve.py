import ast

def is_ordered(pair):
    
        
    return True

def part1(data):
    data = data.split("\n\n")
    pairs = []
    for i, pair in enumerate(data):
        left, right = pair.split("\n")
        left = ast.literal_eval(left)
        right = ast.literal_eval(right)
        pairs.append((left,right))
        
    ordered = []
    for pair in pairs:
        ordered.append(is_ordered(pair))
    count = 0
    for i in range(len(ordered)):
        if ordered[i]:
            count += i+1
    print(ordered)
    return count

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()
res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
