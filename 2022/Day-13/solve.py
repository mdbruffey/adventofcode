def is_ordered(pair):
    left, right = pair.split("\n")
    left = left.strip("][").split(",")
    print(left)
    right = right.strip("][").split(",")
    print(right)
    print("\n")
    if len(left) > len(right):
        return False
    for i in range(len(left)):
        if type(left[i]) != list and type(right[i]) != list:
            if  left[i] > right [i]:
                return False
        elif type(left[i]) == list and type(right[i]) != list:
            if left[i][0] > right[i]:
                return False
        elif type(left[i]) != list and type(right[i]) == list:
            if left[i] > right[i][0]:
                return False
        else:
            for j in range(left[i]):
                if left[i][j] > right[i][j]:
                    return False
                elif left[i][j] < right[i][j]:
                    return True
    return True

def part1(data):
    pairs = data.split("\n\n")
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
